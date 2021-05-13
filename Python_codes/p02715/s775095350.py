n, k = map(int, input().split())
mod = 10**9+7
ans = 0
li = [None]*(k+1)
for i in range(k, 0, -1):
    tmp = pow(k//i, n, mod)
    for j in range(2*i, k+1, i):
        tmp -= li[j]
    li[i] = tmp
    ans += tmp*i
print(ans%mod)