n = int(input())
a = list(map(int, input().split()))
odd = 0
for aa in a:
    if aa % 2 == 1:
        odd += 1
if odd % 2 == 0:
    print('YES')
else:
    print('NO')
