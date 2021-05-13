n=int(input())
a=list(map(int,input().split()))

a.sort()
a.reverse()

ans=0
cnt=0

for i in range(len(a)):
  if i%2==1:
    ans+=a[i]
    cnt+=1

  if cnt==n:
    break

print(ans)