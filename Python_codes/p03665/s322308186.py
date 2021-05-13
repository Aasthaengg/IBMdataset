def main():
  import math
  n,p=map(int,input().split())
  a=list(map(int,input().split()))
  x=[i for i in a if i%2==0]
  y=[i for i in a if i%2==1]
  
  def comb(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
  
  xl,yl=len(x),len(y)
  ans=0
  
  for i in range(xl+1):
    for j in range(yl+1):
      if j%2==p:
        ans+=comb(yl,j)*comb(xl,i)
        
  print(ans)
if __name__=='__main__':
  main()