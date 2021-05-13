n = int(input())
a_list = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 0
for i in range(60):
    k = sum(a >> i & 1 for a in a_list)
    ans += (k * (n - k) % mod) * ((1 << i) % mod) % mod
print (ans % mod)
