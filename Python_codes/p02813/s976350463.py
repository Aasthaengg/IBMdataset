import itertools
import math
N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

P=[]
Q=[]
for i in itertools.permutations(p):
    P.append(i)
for i in itertools.permutations(q):
    Q.append(i)
P=sorted(P)
Q=sorted(Q)
p=tuple(p)
q=tuple(q)
for i in range(math.factorial(N)):
    if P[i]==p:
        a=i+1
        break
for i in range(math.factorial(N)):
    if Q[i]==q:
        b=i+1
        break

print(abs(a-b))

