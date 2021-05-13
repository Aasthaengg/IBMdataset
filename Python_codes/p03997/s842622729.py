import sys
import math
 
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
 
def main():
  a = int(input())
  b = int(input())
  h = int(input())
  
  print(int((a+b)*h/2))
    
if __name__ == '__main__':
    main()