#temprate
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#temprate
N = int(input())
A = inputlist()
B = inputlist()
C = [A[i]-B[i] for i in range(N)]
s = sum(C)
if s < 0:
    print(-1)
    exit()
C.sort()
ans = 0
for i in range(N):
    if C[i] <0:
        pass
    elif C[i] <= s:
        ans +=1
        s -= C[i]
    else:
        break
print(N-ans)