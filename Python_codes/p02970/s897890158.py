import math
def main():
  n,d = list(map(int,input().split()))
  if n %(2*d+1)==0:
    print(int(n /(2*d+1)))
  else:
    print(int(n /(2*d+1))+1)
main()