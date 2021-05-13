import collections
N=int(input())
D=list(map(int,input().split()))
E=collections.Counter(D)
M=int(input())
T=list(map(int,input().split()))
F=collections.Counter(T)
r='YES'
for u in F.keys():
     if E[u] < F[u]:
         r='NO'
print(r)
