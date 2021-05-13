import sys
N = int(input())
a = list(map(int, input().split()))
C = [0] * 3
for ai in a:
    if ai % 4 == 0:
        C[2] += 1
    elif ai % 2 == 0:
        C[1] += 1
    else:
        C[0] += 1
while C[0] > 0:
    if C[2] > 0:
        C[0] -= 1
        C[2] -= 1
    else:
        if C[0] == 1 and C[1] == 0:
            print('Yes')
            sys.exit()
        else:
            print('No')
            sys.exit()
print('Yes')