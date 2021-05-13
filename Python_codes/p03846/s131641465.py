n=int(input())
mod=10**9+7
A=list(map(int,input().split()))

from collections import Counter
C=Counter(A)
if n%2==0:
    for i in range(1,n,2):
        if C.get(i) != 2:
            print(0);exit()
else:
    if C.get(0) !=1:
        print(0);exit()
    for i in range(2,n,2):
        if C.get(i)!=2:
            print(0);exit()

n//=2
print(pow(2,n,mod))