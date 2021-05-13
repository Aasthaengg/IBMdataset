n=int(input())
t,a=map(int,input().split())
H=list(map(int,input().split()))
minn=10**10
for i in range(n):
  if minn>abs((t*(1000)-6*H[i])-a*1000):
    ans = i
    minn=abs((t*(1000)-6*H[i])-a*1000)
print(ans+1)
