import sys
a=list(map(int,input().split()))
a.sort()
if a[0]%2==0 or a[1]%2==0 or a[2]%2==0:
    print(0)
    sys.exit()
ans=a[0]*a[1]
print(ans)