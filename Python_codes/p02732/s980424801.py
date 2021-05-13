from collections import Counter
N, = list(map(int,input().split()))
A  = list(map(int,input().split()))
c = Counter(A)
p = sum([(c[k]*(c[k]-1)//2) for k in c.keys()])
for ai in A:
    print(p - c[ai] + 1)