n = int(input())
p = list(map(int, input().split()))
ch = 0
for i in range(n):
    if (i+1) != p[i]:
        ch += 1

if ch > 2:
    print('NO')
else:
    print('YES')
