from math import factorial
N,A,B = map(int,input().split())
V = sorted(list(map(int,input().split())),reverse=True)
C = {}
for i in range(N):
    if V[i] not in C:
        C[V[i]] = 0
    C[V[i]] += 1
v = V[A-1]
avg = sum(V[:A])/A
print(avg)
cnt = V[:A].count(v)
if cnt<A:
    tot = factorial(C[v])//factorial(cnt)//factorial(C[v]-cnt)
else:#cnt==A
    tot = 0
    for j in range(A,min(B,C[v])+1):
        tot += factorial(C[v])//factorial(j)//factorial(C[v]-j)
print(tot)