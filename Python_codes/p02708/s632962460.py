n,k = map(int, open(0).read().split())

left = right = 0
ans = 0
MOD = 10**9+7

for c,(i,j) in enumerate(zip(range(n+1), range(n,-1,-1))):
    left += i
    right += j
#     print(i,j, right, left,c)
    if c >= k-1:
        ans += (right-left+1)
        ans %= MOD

print(ans)