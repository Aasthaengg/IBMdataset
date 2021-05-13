def main():
  n,l = list(map(int,input().split()))
  ans=0
  if l>=0:
    for i in range(2,n+1):
      ans+= l+i-1
  elif n+l-1<0:
    for i in range(1,n):
      ans+=l+i-1
  else:
    for i in range(1,n+1):
      ans+=l+i-1
  print(ans)  
main()