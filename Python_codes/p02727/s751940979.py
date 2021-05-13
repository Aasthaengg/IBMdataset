X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

red = [[i, "r"] for i in p]
green = [[i, "g"] for i in q]
white = [[i, "w"] for i in r]

total = sorted(red + green + white)[::-1]

ans = 0
cnt = 0
r_cnt = 0
g_cnt = 0
for t in total:
    if t[1] == "r" and r_cnt == X:
        continue
    if t[1] == "g" and g_cnt == Y:
        continue
    ans += t[0]
    if t[1] == "r":
        r_cnt += 1
    elif t[1] == "g":
        g_cnt += 1
    cnt += 1
    if cnt == X + Y:
        break

print(ans)