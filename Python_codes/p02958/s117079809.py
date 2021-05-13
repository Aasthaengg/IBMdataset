n = int(input())
p = list(map(int, input().split()))
w = list(range(1,n+1))
t = 0
for i in range(n):
    if p[i] != w[i]:
        t += 1
if 0 <= t <= 2:
    print('YES')
else:
    print('NO')