def chk(s,x,y):
    cnt = 0
    if s[y][x]!='#':
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0<=x+i<w and 0<=y+j<h:
                    if s[y+j][x+i]=='#':
                        cnt += 1
        return str(cnt)
    else:
        return '#'

h,w = map(int,input().split())
gazo = []
for i in range(h):
    gazo.append(str(input()))

#for i in range(h):
#    print(gazo[i])

for i in range(h):
    for j in range(w):
        print(chk(gazo,j,i),end='')
    print('')

