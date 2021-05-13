N=int(input())
A=list(map(int,input().split()))
from collections import defaultdict
numsubs=defaultdict(int)
for sub in A:
    numsubs[sub]+=1
for k in range(N):
    print(numsubs[k+1])