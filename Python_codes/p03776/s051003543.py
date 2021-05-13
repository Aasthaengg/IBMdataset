import math
def comb(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

n, a, b = map(int,input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)
max_avg = sum(v[:a]) / a
min_v = min(v[:a])

ans = 0
for i in range(a, b+1):
    if max_avg != sum(v[:i]) / i: break
    cnt1 = v[:i].count(min_v)
    cnt2 = v.count(min_v)
    ans += comb(cnt2, cnt1)

print(max_avg)
print(int(ans))