n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

tt = []
prev = 0
for e in t:
    if e > prev:
        tt.append([e, e])
        prev = e
    else:
        tt.append([1, e])

aa = []
prev = 0
for e in a[::-1]:
    if e > prev:
        aa.append([e, e])
        prev = e
    else:
        aa.append([1, e])
aa = aa[::-1]

ans = 1
for et, ea in zip(tt, aa):
    mn = max(et[0], ea[0])
    mx = min(et[1], ea[1])
    ans *= max(0, mx - mn + 1)
    ans %= mod

print(ans)
