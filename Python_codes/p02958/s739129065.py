n = int(input())
p = list(map(int, input().split()))

judge = 0
for i in range(n):
    if p[i] != i + 1:
        judge += 1
if judge >= 3:
    print('NO')
else:
    print('YES')
