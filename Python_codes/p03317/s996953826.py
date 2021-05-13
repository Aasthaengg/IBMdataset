from math import ceil
n,k=map(int,input().split())
a=list(map(int,input().split()))
n-=1
k-=1
print(ceil(n/k))