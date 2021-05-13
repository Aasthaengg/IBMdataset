a,b = map(int, input().split())

N=100
ans = [["#" for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N//2,N):
        ans[j][i]="."

for i in range(0,N,2):
    if a==1:
        break
    for j in range(0,N,2):
        ans[i][j]="."
        a-=1
        if a==1:
            break

for i in range(1+N//2,N,2):
    if b==1:
        break
    for j in range(0,N,2):
        ans[i][j]="#"
        b-=1
        if b==1:
            break

print(100,100)
for i in range(N):
    print(*ans[i],sep="")