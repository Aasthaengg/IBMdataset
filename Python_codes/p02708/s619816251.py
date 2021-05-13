n, k = map(int, input().split())
mod = pow(10,9)+7
ans = 0
l, h = 0, 0
for i in range(1,n+2):
    l += i-1
    h += n-i+1
    if i>=k: ans += (h-l+1)%mod
print(ans%mod)