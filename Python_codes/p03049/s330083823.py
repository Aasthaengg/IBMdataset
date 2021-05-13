import sys
n = int(input())
ans, c, h, t = 0, 0, 0, 0

for x in sys.stdin.readlines():
    x = x.rstrip()
    ans += x.count("AB")
    if x[-1] == "A" and x[0] == "B":
        c += 1
    elif x[-1] == "A":
        t += 1
    elif x[0] == "B":
        h += 1
if t + h > 0:
    ans += min(t, h) + c
elif c > 0:
    ans += c-1
print(ans)