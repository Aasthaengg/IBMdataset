import sys
sys.setrecursionlimit(10**6)

a,b,k=map(int,input().split())

i=0
for j in range(max(a,b),0,-1):
    if a%j==0 and b%j==0:
        i+=1
    if i==k:
        print(j)
        exit()

