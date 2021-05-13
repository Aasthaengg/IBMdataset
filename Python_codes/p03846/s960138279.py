n=int(input())
l=sorted(map(int,input().split()))[::-1]
def f(x):
  t=n+1
  for i in l[x::2]:
    if t-2!=i: return 0
    t=i
  return 1
print(pow(2,n//2,10**9+7)*f(0)*f(1))