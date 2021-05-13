A, B = list(input().split())
s = B.strip().split(".")
a = int(s[0]) * (10 ** 2)
if len(s) > 1:
    t = s[1] + "0" * (2 - len(s[1]))
    a += int(t)
a = int(a)
ans = a * int(A) // 100
print(ans)