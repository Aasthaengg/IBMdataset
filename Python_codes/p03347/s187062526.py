import sys
def input():
    return sys.stdin.readline()[:-1]
n=int(input())
a=[int(input()) for i in range(n)]
if a[0]!=0:
    print(-1)
    quit()
ans=0
for i in range(n-1):
    if a[i+1]-a[i]>1:
        print(-1)
        quit()
    elif a[i+1]-a[i]==1:
        ans+=1
    else:
        ans+=a[i+1]
print(ans)