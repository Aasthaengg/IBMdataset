s = input()
t = input()
cnt = 0
for i, c in enumerate(s):
    if t[i] != c: cnt += 1
print(cnt)