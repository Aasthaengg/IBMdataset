N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
import math
def num(P):
    l = list(range(N+1))
    l.remove(0)
    p = 1
    for i in range(N):
        p += l.index(P[i]) * math.factorial(N-1-i)
        l.remove(P[i])
    return p
ans = num(P) - num(Q)
print(abs(ans))