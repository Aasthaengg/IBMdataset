from collections import defaultdict
count=defaultdict(lambda:0)
N=int(input())
A=list(input().split(" "))
k=-1
for i in range(N):
    count[A[i]]+=1
if N%2==1:
    if count["0"]!=1:
        k=0
    for i in range(1,N//2+1):
        if count[str(2*i)]!=2:
            k=0
else:
    for i in range(1,N//2+1):
        if count[str(2*i-1)]!=2:
            k=0
if k!=0:
    if N%2==0:
        print(2**(len(count.keys()))%(10**9+7))
    else:
        print(2**(len(count.keys())-1)%(10**9+7))
else:
    print(0)