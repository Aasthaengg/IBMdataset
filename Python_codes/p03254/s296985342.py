n,x = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
f = 0
for i in range(n):
    if x-a[i]>=0:
        ans+=1
        x-=a[i]
    else:
        f = 1
        break
if x>0 and f==0:
    ans-=1
print(ans)