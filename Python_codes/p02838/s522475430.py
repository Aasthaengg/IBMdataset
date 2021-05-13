def mi(): return map(int,input().split())
def lmi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()

n=ii()
a=lmi()
INF=10**9+7
ans=0
for i in range(60):
  x=0
  for j in range(n):

    if (a[j]>>i)&1:
      x+=1

  num=x*(n-x)*2**i
  ans+=num

print(ans%INF)