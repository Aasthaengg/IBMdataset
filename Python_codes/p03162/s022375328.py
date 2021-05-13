import sys
input=sys.stdin.readline
n=int(input())

a=[None]*n
b=[None]*n
c=[None]*n
for i in range(n):
    a[i],b[i],c[i]=map(int,input().split())

dpa=[a[0]]+[None]*(n-1)
dpb=[b[0]]+[None]*(n-1)
dpc=[c[0]]+[None]*(n-1)

for i in range(1,n):
    dpa[i]=a[i]+max(dpb[i-1],dpc[i-1])
    dpb[i]=b[i]+max(dpa[i-1],dpc[i-1])
    dpc[i]=c[i]+max(dpa[i-1],dpb[i-1])

print(max(dpa[-1],dpb[-1],dpc[-1]))