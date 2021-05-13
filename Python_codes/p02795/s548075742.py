import math
if __name__=='__main__':
   H=int(input())
   W=int(input())
   N=int(input())
   t = math.ceil(N/(H if H>W else W))
   print (t)