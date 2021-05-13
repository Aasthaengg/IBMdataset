n = int(input())
ans = 0
a, b, ab = 0, 0, 0
for _ in range(n):
    s = list(input())
    l = len(s)
    for i in range(l - 1):
        if s[i] == "A" and s[i + 1] == "B":
            ans += 1
    if s[0] == "B":
        b += 1
    if s[l - 1] == "A":
        a += 1
    if s[0] == "B" and s[l - 1] == "A":
        ab += 1
if a == b == ab:
    a -= 1
ans += min(n - 1, max(0, min(a, b)))
print(ans)