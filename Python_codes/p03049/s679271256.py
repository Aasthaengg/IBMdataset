n = int(input())
ans = 0
a = 0
b = 0
ba = 0
for i in range(n):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A":
        if s[0] == "B":
            ba += 1
        a += 1
    if s[0] == "B":
        b += 1
if a > b:
    ans += b
elif b > a:
    ans += a
else:
    ans += a
    if a == ba and a > 0:
        ans -= 1
print(ans)
