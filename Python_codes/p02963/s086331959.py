def main():
  s=int(input())
  max=pow(10,9)
  if s<=max:
    x1,y1,x2,y2,x3,y3=0,0,s,0,s,1
  elif s%max==0:
    x1,y1,x2,y2,x3,y3=0,0,max,0,max,s//max
  else:
    a=s%max
    b=s//max
    x1,y1,x2,y2,x3,y3=0,0,max, 1,max-a,b+1
  print(x1,y1,x2,y2,x3,y3)
  #print(ss(x2,y2,x3,y3))
def ss(x2,y2,x3,y3):
  return x2*y3-x3*y2
if __name__=='__main__':
  main()
