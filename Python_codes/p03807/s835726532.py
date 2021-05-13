N = int(input())

a = list(map(int,input().split()))
odd = 0
for i in range(N):
    if a[i] % 2:
        odd += 1
if odd % 2:
    print('NO')
else:
    print('YES')