s = input()
m = 0
cnt = 0
for i in range(len(s)):
    if s[i] in ['A','T','C','G']:
        cnt += 1
        m = max(m,cnt)
    else:
        cnt = 0
print(m)
