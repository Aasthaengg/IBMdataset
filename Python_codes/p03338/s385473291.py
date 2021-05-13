import string

n = int(input())
s = input()
alp = list(string.ascii_lowercase)
ans = 0

for i in range(n):
    s1 = s[:i]
    s2 = s[i:]
    cnt = 0
    for c in alp:
        if c in s1 and c in s2:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
