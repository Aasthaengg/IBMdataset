N = int(input())
A = list(map(int,input().split()))
Odd = 0
Even = 0
for Ai in A:
    if Ai % 2 == 0:
        Even += 1
    else:
        Odd += 1
if Odd % 2 == 1:
    print('NO')
else:
    print('YES')