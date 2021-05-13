s = list(input())
t = 'CODEFESTIVAL2016'
cnt = 0
for i in range(len(s)):
    if s[i] != t[i]:
        cnt += 1

print(cnt)