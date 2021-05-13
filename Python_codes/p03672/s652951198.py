s = input()
n = len(s)
idx = 1
while idx < n:
    sub_s = s[: n - idx]
    if sub_s == sub_s[: len(sub_s) // 2] * 2:
        break
    idx += 1

print(n - idx)

