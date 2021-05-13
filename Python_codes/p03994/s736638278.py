s = [ord(x) - ord("a") for x in input()]
k = int(input())

for i, r in enumerate(s):
    if r == 0:
        pass
    elif 26 - r <= k:
        k -= 26-r
        s[i] = 0

if k > 0:
    k %= 26
    s[-1] += k

ans = ""
for r in s:
    ans += chr(ord("a") + r)

print(ans)

