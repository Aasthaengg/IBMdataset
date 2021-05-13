import sys
def input():
    return sys.stdin.readline()[:-1]
n,m,d=map(int,input().split())

ans=0
if d!=0:
    ans=(n-d)*2*(m-1)/n/n
else:
    ans=n*(m-1)/n/n
print(ans)