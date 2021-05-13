import math
def main():
  a,b,n=map(int,input().split())
  if(b>n):
    print(math.floor(a*n/b)-a*math.floor(n/b))
    return
  if(n>=b):
    print(math.floor(a*(b-1)/b)-a*math.floor((b-1)/b))
    return
    
main()