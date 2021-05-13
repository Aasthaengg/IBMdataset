K, S = map(int, input().split())

l = max(S-K*2, 0)
h = min(K, S)

res = 0
for i in range(l, h+1):
    x = S-i
    ll = max(x-K, 0)
    hh = min(h, x)
    res += hh-ll+1

print(res)