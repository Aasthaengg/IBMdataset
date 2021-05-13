N=int(input())
L = [None]*N
for i in range(N):
    L[i] = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans+=(L[i][1]-L[i][0]+1)

print(ans)
