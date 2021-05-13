import sys
input = sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
A.sort()
from collections import Counter
c=Counter(A).items()
#print(c)
cnt=0
for key,val in c:
    if val%2==0:
        cnt+=1
print(len(c) if cnt%2==0 else len(c)-1)
