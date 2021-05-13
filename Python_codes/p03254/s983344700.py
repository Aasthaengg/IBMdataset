N,x = map(int,input().split())
a=list(map(int,input().split()))

a.sort()

ans=0
for i in range(N):
    if x == 0:
        break
    if x >= a[i]:
        ans+=1
        x-=a[i]
    else:
        x = 0
if x != 0:
    ans -= 1
print(max(0,ans))
