n = int(input())
s = [input() for _ in range(n)]

a = 0
b = 0
ba = 0
ans = 0
for v in s:
    ans += v.count("AB")
    if v[0] == "B" and v[-1] == "A":
        ba += 1
    elif v[0] == "B":
        b += 1
    elif v[-1] == "A":
        a += 1

ans += max(0, ba - 1)
if ba:
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1

ans += min(a, b)

print(ans)