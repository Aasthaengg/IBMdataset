s = input()
t = input()
cnt = 0
for c1, c2 in zip(s, t):
    if c1 != c2:
        cnt += 1
    else:
        pass
print(cnt)