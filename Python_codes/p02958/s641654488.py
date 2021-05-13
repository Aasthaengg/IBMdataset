N = int(input())
P = list(map(int, input().split()))
ctr = 0
for i in range(N):
    if P[i] != i+1:
        ctr += 1
if ctr <= 2:
    print('YES')
else:
    print('NO')