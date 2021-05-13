s = list(input())
n = len(s)
l = s[: (n - 1) // 2]
r = s[(n + 1) // 2 :]
if l == l[::-1] and r == r[::-1] and s == s[::-1]:
    print("Yes")
else:
    print("No")
