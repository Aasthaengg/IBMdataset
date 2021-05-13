n, a, b = map(int, input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)

maximum = sum(v[:a])

print(maximum / a)

def comb(n, r):
    if n - r < r:
        r = n - r
    if r < 0:
        return 0
    ans = 1
    for i in range(r):
        ans *= n - i
    for i in range(1, r+1):
        ans //= i
    return ans

# 選ぶ品物の価値が全て等しい時
if v[0] == v[a-1]:
    num = v.count(v[0])
    ans = 0
    for i in range(a, b+1):
        ans += comb(num, i)
    print(ans)
else:
    num = v.count(v[a-1])
    r = v[:a].count(v[a-1])
    print(comb(num, r))