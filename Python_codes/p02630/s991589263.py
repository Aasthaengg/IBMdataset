N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i] = map(int,input().split())
    
import collections
c = collections.Counter(A)
startsum = sum(A)
for i in range(Q):
    Bcount = c[B[i]]
    c[B[i]] = 0
    Ccount = c[C[i]]
    c[C[i]] += Bcount
    startsum += (C[i]-B[i])*Bcount
    print(startsum)