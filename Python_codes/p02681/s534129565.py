s = input()
t = input()

n = 0
cnt = 0

for i in range(len(s)):
    if s[i] != t[n]:
        cnt += 1
    n += 1

if cnt == 0:
    print('Yes')
else:
    print('No')