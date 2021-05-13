from collections import defaultdict
N,T=list(map(int,input().split(" ")))
A=list(map(int,input().split(" ")))
sub=defaultdict(lambda:0)
max1=A[0]
min1=A[0]
for i in range(N):
    if A[i]>=max1>=min1:
        max1=A[i]
        sub[max1-min1]+=1
    elif max1>=A[i]>=min1:
        max1=A[i]
        sub[max1-min1]+=1
    elif min1>=A[i]:
        min1=A[i]
        max1=A[i]
a=list(sub.keys())
b=max(a)
print(sub[b])