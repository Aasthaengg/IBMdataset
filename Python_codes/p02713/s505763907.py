def main():
  import math
  N = int(input())
  gcd={}
  ans=0
  for i in range(1,N+1):
    for j in range(1, N+1):
      key=i*N+j
      gcd[key]=math.gcd(i,j)
  
  for k, i in gcd.items():
    for j in range(1, N+1):
      key=j*N+i
      ans+=gcd[key]
        
  print(ans)
 
if __name__=='__main__':
  main()