s = str(input())
t = s[::-1]
n = len(s)
cnt = 0
for i in range((n+1)//2):
    if s[i] != t[i]:
        cnt += 1
print(cnt)