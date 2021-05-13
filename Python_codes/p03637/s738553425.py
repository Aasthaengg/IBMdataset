n = int(input())
A = tuple(map(int, input().split()))
c4 = 0
c2 = 0
cn = 0
for a in A:
    if a%4==0:
        c4 += 1
    elif a%2==0:
        c2 += 1
    else:
        cn += 1

if c2 == 0 or c2 == 1:
    if cn+c2 <= c4 + 1:
        print('Yes')
    else:
        print('No')
else:
    if cn <= c4:
        print('Yes')
    else:
        print('No')
