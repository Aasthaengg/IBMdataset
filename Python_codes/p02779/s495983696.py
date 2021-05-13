n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
m = len(b)
if n == m:
    print('YES')
else:
    print('NO')