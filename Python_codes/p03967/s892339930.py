s = input()
cnt = 0
for i, c in enumerate(s):
    if i % 2 == 0:
        if c == 'p':
            cnt -= 1
    else:
        if c == 'g':
            cnt += 1
print(cnt)