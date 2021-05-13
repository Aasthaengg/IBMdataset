n= int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

from collections import Counter
C = Counter(D)
for t in T:
    if t not in C:
        print('NO')
        exit()
    else:
        if C[t] == 0:
            print('NO')
            exit()
        else:
            C[t] -= 1
else:
    print('YES')
