n = int(input())
s = list(input())
t = list(input())
cnt = 0
for i in range(min(len(s), len(t))):
    c = 0
    for j in range(i + 1):
        if s[len(s) - 1 - i + j] == t[j]:
            c += 1
    cnt = max(cnt, c)
ans = len(s) + len(t) - cnt
if ans < n:
    ans = n
print(ans)