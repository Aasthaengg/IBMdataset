def main():
  n,k=map(int,input().split())
  s=input()
  
  # first score
  ans=0
  x=s[0]
  for i in range(1,n):
    if x==s[i]:
      ans+=1
    else:
      x=s[i] 
  print(min(ans+2*k,n-1))

  
if __name__=='__main__':
  main()