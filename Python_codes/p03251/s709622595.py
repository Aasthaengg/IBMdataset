import math
def main():
  n,m,x,y = list(map(int,input().split()))
  xv = list(map(int,input().split()))
  yv = list(map(int,input().split()))
  flg=0
  if max(xv)<=min(yv):
    for i in range(x+1,y+1):
      if(max(xv) < i )and(i <= min(yv)):
        flg=1
        break
  if flg==1:
    print("No War")
  else:
    print("War")
    
main()