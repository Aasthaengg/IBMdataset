import sys
input=sys.stdin.readline

n,k=map(int,input().split())
lst=[0]*100001

for i in range(n):
    a,b=map(int,input().split())
    lst[a]+=b

for i in range(100001):
    k-=lst[i]
    if k<=0:
        print(i)
        break