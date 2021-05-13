s, t = [input() for i in range(2)]
cnt = 0
for i in range(3):
    if s[i] == t[i]: cnt += 1
print(cnt)