n=int(input())
A=[]
for i in range(n):
    A.append(input())
import collections
B = collections.Counter(A)
C=list(set(A))
cnt=0
for j in range(len(C)):
    if B[C[j]] %2 != 0:
        cnt+=1
print(cnt)