from math import ceil
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
n=n-k
c=1
if(n>0):
    c+=ceil(n/(k-1))
print(c)