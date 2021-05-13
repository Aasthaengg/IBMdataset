s = input()
t = input()

cnt = 0
for s1, s2 in zip(s, t):
    if s1 != s2:
        cnt = cnt + 1
print(cnt)