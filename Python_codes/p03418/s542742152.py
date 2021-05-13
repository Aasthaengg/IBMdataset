def main():
  n,k=map(int,input().split())
  r=0
  for q in range(n+1):
      if q==0:
          for b in range(1,n+1):r+=max(min(b,k)-1,0)
      else:
          for b in range(1,n//q+1):r+=min(k,n-q*b+1,b)
  print(n*n-r)

if __name__=="__main__":
  main()