import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,K = MI()
xy = [tuple(MI()) for i in range(N)]

xy.sort()

from operator import itemgetter

ans = 10**19
for i in range(N-1):
    for j in range(i+1,N):
        a = xy[j][0]-xy[i][0]
        A = xy[i:j+1]
        if len(A) >= K:
            A = sorted(A, key=itemgetter(1))
            b = 10**18
            for k in range(len(A)-K+1):
                b = min(b,A[k+K-1][1]-A[k][1])
            ans = min(ans,a*b)

print(ans)
