import math
def main():
  a=int(input())
  b=int(input())
  c=int(input())
  x=int(input())
  ans=0
  for i in range(0,a+1):
    for j in range(0,b+1):
      for k in range(0,c+1):
        if i*500+j*100+50*k==x:
          ans+=1
  print(ans)
  
main()
