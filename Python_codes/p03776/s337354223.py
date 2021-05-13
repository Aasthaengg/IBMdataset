from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N,A,B=map(int,input().split())
V=list(map(int,input().split()))
V.sort()
av_max=0
count=0

for i in range(A,B+1):
    if sum(V[N-i:N])/i>av_max:
        av_max=sum(V[N-i:N])/i
        count=cmb(V.count(V[N-i]),V[N-i:N].count(V[N-i]))
    elif sum(V[N-i:N])/i==av_max:
        count+=cmb(V.count(V[N-i]),V[N-i:N].count(V[N-i]))

print(av_max)
print(count)