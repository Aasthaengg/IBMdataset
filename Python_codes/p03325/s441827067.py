n=int(input())
a=list(map(int,input().split()))

def tw(n):
  ret=0
  while n%2==0:
    n/=2
    ret+=1
  return ret

ans=0
for i in a:
  ans+=tw(i)

print(ans)