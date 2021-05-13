n=int(input())
a=list(map(int,input().split()))

def check(n):
  cnt=0
  while n%2==0:
    n=n//2
    cnt=cnt+1
  return cnt

ans=0
for i in a:
  ans=ans+check(i)
  
print(ans)
