N, T = map(int, input().split(" "))
t = list(map(int, input().split(" ")))

before = t[0]
ans = 0
for ti in t[1:]:
    if ti - before <= T:
        ans += ti - before
    else:
        ans += T
    before = ti
print(ans + T)