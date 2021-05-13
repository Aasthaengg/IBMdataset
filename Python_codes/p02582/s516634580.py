s = input().strip()
res, tmp = 0, 0

for c in s:
    if c == 'R':
        tmp += 1
        res = max(res, tmp)
    else:
        tmp = 0

print(res)