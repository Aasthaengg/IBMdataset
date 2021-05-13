s = input()
n = len(s)
ans = 1000000000
keep = 0

for i in range(n):
    check = 0
    keep = 0
    for j in range(n):
        if s[i] != s[j]:
            check += 1
        else:
            check = 0
        keep = max(check, keep)
    ans = min(ans, keep)
print(ans)
