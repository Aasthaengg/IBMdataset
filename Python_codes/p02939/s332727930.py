s = input()
n = len(s)
i = 0
ans = n
while i < n - 1:
    if s[i] == s[i + 1]:
        ans -= 1
        i += 2
    i += 1
print(ans)
