import math
def main():
  x1,y1,x2,y2 = list(map(int,input().split()))
  xsub=x2-x1
  ysub=y2-y1
  print(x2-ysub,y2+xsub,x1-ysub,y1+xsub)
main()