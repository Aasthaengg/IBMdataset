n=int(input())
S=[0 if i=='.' else 1 for i in input()]
if sum(S)==0 or sum(S)==n:
    print(0)
    exit()
sS=sum(S)
allblack=n-sum(S)
allwhite=sum(S)
bw=10**6
from itertools import accumulate
accS=list(accumulate(S))
for i in range(n):
    bw=min(bw,accS[i]+(n-(i+1))-(sS-accS[i]))
print(min(bw,allblack,allwhite))