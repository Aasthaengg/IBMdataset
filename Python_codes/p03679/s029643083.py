import sys
import math
 
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
 
def main():
  x,a,b = map(int, input().split())
  
  if b-a <= 0:
    print("delicious")
  elif b-a >0 and b-a <= x:
    print("safe")
  else:
    print("dangerous")
    
if __name__ == '__main__':
    main()