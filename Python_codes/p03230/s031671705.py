from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime,random
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N = int(input())
tmp = 0
cnt = 0
while True:
    cnt += 1
    tmp += cnt
    if N == tmp:
        break
    elif N < tmp:
        print('No')
        sys.exit()

print('Yes')
print(cnt+1)
M = cnt

B = [1]
Bs = 1
for k in range(M,1,-1):
    Bs += k
    B.append(Bs)
B.sort()
#print(B)

S =[[] for _ in range(M+1)]
for i in range(1,N+1):
    ind = bisect.bisect_right(B,i)
    #print(i,ind,B[ind-1])
    S[ind-1].append(i)
    S[ind+(i-B[ind-1])].append(i)

for i in range(M+1):
    print (' '.join(map(str,[M]+S[i])))
