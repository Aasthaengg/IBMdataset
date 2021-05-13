N = int(input())
A = list(map(int, input().split()))

odd = 0
for a in A:
    if a % 2:
        odd += 1
if odd % 2:
    print('NO')
else:
    print('YES')