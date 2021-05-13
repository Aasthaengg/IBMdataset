s = str(input())
s = s.replace('BC', 'D')
n = len(s)

ans = 0
cnt = 0
for i in range(n):
    if s[i] == 'A':
        cnt += 1
    if s[i] == 'D':
        ans += cnt
    if s[i] == 'B' or s[i] == 'C':
        cnt = 0
print(ans)