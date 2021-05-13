from collections import Counter
N,M=map(int,input().split())
A=sorted(map(int,input().split()),reverse=True)
s=sum(A)/(4*M)
for i in range(M):
    if A[i]<s:
        print('No')
        exit()
print('Yes')