import sys
from itertools import combinations
def I(): return int(sys.stdin.readline().rstrip())


N = I()
A = [(i*(i-1))//2 for i in range(448)]

index = 0
for i in range(2,448):
    if A[i] == N:
        print('Yes')
        print(i)
        index = i
        break
else:
    print('No')
    exit()

ANS = [[index-1] for _ in range(index)]
for i,a in enumerate(list(combinations([i for i in range(index)],2))):
    b,c = a
    ANS[b].append(i+1)
    ANS[c].append(i+1)

for ans in ANS:
    print(*ans)

