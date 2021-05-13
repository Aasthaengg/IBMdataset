N = int(input())
A = list(map(int,input().split()))

ave = 0
for i in range(N):
    ave += A[i]

ave = ave/N

ans = 0
m = 10**8
for i in range(N):
    tmp = A[N-1-i]
    res = abs(tmp-ave)
    if res<=m:
        m = res
        ans = N-1-i
print(ans)