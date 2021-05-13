n=int(input())
def f(x):
  tmp=(n//x)*(n//x+1)//2
  return x*tmp

ans=sum(map(f,range(1,n+1)))
print(ans)