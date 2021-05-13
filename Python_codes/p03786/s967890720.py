import sys
def input(): return sys.stdin.readline().strip()
n=int(input())
a=sorted(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i]*2<a[i+1]:
        c=i+1
    a[i+1]+=a[i]
print(n-c)