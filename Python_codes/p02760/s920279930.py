a=[list(map(int,input().split())) for _ in range(3)]
n=int(input())
b=[int(input()) for _ in range(n)]
used=[[False]*3 for _ in range(3)]
for k in range(n):
    for i in range(3):
        for j in range(3):
            if a[i][j]==b[k]:
                used[i][j]=True

for i in range(3):
    if used[0][i] and used[1][i] and used[2][i]:
        print("Yes")
        exit()
        
for i in range(3):
    if used[i][0] and used[i][1] and used[i][2]:
        print("Yes")
        exit()

if used[0][0] and used[1][1] and used[2][2]:
        print("Yes")
        exit()

if used[0][2] and used[1][1] and used[2][0]:
        print("Yes")
        exit()                
print("No")