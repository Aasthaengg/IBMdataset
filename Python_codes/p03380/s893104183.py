import sys
sys.setrecursionlimit(2147483647)

n=int(input())
aa=list(map(int,input().split()))

if n==2:
    print(aa[0],aa[1])
    exit()

aa.sort()

nn=max(aa)

c=0
tmp=10**9

for a in aa:
    if abs(nn/2.0-a)<tmp:
        tmp=abs(nn/2.0-a)
        c=a

print(nn,c)

     
