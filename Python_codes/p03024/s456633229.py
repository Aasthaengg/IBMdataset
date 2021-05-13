s=list(input())
res = len(s)-s.count('x')+(15-len(s))
if res > 7:
    print('YES')
else:
    print('NO')