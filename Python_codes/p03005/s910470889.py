import sys
input = sys.stdin.readline
#n = int(input()) 
n,k = (int(i) for i in input().split())
if k==1:
    ans=0
else:
    res=n-(k-1)
    ans=res-1
print(ans)