N=int(input())

A=list(map(int,input().split()))

NA=[]

for i in range(N):
    NA.append(A[i]-i)

from collections import Counter

d=Counter(NA)

cnt=0
for i in range(N-1):
    cnt+=d[-i-A[i]]

print(cnt)

