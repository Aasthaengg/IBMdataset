s = input()
l = len(s)
cnt = 0
for i in range(1, l):
    if s[i] != s[i - 1]:
        cnt += 1
print(cnt)