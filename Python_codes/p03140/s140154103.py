N=int(input())
A=list(input())
B=list(input())
C=list(input())

import collections

cnt=0

for i in range(N):
    tmp=[]
    tmp.append(A[i])
    tmp.append(B[i])
    tmp.append(C[i])
    c = collections.Counter(tmp)
    values, counts = zip(*c.most_common())
    cnt+=3-counts[0]

print(cnt)