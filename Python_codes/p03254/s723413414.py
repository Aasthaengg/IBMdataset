n, x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ans=0

for a in A:
    x-=a
    if x>=0:
        ans+=1
    else:
        break

if x>0:
    ans-=1

print(ans)