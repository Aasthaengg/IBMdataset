n = int(input())
p = list(map(int,input().split()))
r = list(range(1,n+1))
t = 0

for i in range(n):
    if p[i] != r[i]:
        t += 1

if t > 2:
    print('NO')
else:
    print('YES')