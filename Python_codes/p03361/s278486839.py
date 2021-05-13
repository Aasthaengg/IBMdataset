H,W=map(int,input().split())
s=[]

for i in range(H):
    a=[i for i in input()]
    s.append(a)


for i in range(H):
    for j in range(W):
        if s[i][j]=='#':
            f=0
            for x,y in [(j,i+1),(j+1,i),(j,i-1),(j-1,i)]:
                if x<0 or x>W-1 or y<0 or y>H-1:
                    continue
                if s[y][x]=='#':
                    f=1
                    break
            if f==0:
                print('No')
                exit()

print('Yes')
