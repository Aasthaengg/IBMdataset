N = int(input())
p = list(map(int, input().split()))
P = sorted(p)

count = 0
for i in range(N):
    if p[i] != P[i]:
        count += 1
if count == 0 or count == 2:
    print('YES')
else:
    print('NO')
