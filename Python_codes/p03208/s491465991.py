n,k = map(int,input().split())
hl = []
for _ in range(n):
    hl.append(int(input()))
hl.sort()

ans = 10**9
for i in range(n-k+1):
    diff = hl[i+k-1] - hl[i]
    ans = min(ans,diff)
print(ans)
