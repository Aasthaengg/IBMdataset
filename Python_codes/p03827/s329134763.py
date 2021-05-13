n = int(input())
s = input()

cnt = 0
m = 0

for i in range(len(s)):
    if s[i] == 'I':
        cnt += 1
        m = max(m, cnt)
    if s[i] == 'D':
        cnt -= 1
        m = max(m, cnt)
print(m)

