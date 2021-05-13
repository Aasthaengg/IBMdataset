a,b,c = map(int,input().split())
n = b - a
m = c - b
if n == m:
    print('YES')
else:
    print('NO')