n,k=map(int,input().split())
a=list(map(int,input().split()))
hantei=10**10+1
for i in range(0,n-k+1):
  #print(a[i],a[i+k-1])
  d=a[i+k-1]-a[i]+min(abs(a[i]),abs(a[i+k-1]))
  if hantei>d:
    hantei=d
print(hantei)