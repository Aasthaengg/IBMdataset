h,w=map(int,input().split())
S=[]
for i in range(h):
    S.append(list(input()))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for i in range(1,h-1):
    for j in range(1,w-1):
        if S[i][j]=='#':
            if all(S[i+dx[k]][j+dy[k]]=='.' for k in range(4)):
                print("No")
                exit()
print("Yes")