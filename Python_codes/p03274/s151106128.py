def main():
  import bisect
  n,k=map(int,input().split())
  x=list(map(int,input().split()))
  ans=abs(x[0])*2+abs(x[-1])*2
  if 0 in x:
    r=x.index(0)
    l=max(0,r-(k-1))
  else:
    r=bisect.bisect_right(x,0)
    l=max(0,r-k)
  ans=2*abs(x[0])+2*abs(x[-1])
  for i in range(l,min(n-k+1,r+1)):
    if x[i]*x[i+k-1]<=0:
      a=min(abs(x[i]),abs(x[i+k-1]))
      b=max(abs(x[i]),abs(x[i+k-1]))
      ans=min(ans,2*a+b)
    else:
      b=max(abs(x[i]),abs(x[i+k-1]))
      ans=min(ans,b)
  print(ans)
if __name__=='__main__':
  main()
