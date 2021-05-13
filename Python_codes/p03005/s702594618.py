import sys

n,k = input().split()
n,k = int(n), int(k)

if k==1 :
    print(0)
else :
    print(n-k)
