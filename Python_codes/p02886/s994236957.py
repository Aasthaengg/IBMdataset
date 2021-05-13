N = int(input())
d = list(map(int,input().split()))
ans = 0
for k in range(N-1):
    for l in range(k+1,N):
        ans += d[k]*d[l]
print(ans)
