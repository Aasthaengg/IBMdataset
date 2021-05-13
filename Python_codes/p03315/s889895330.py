s = list(input())
res = 0
for i in range(0, len(s)):
    if s[i] == "+":
        res += 1
    else:
        res -= 1
print(res)
