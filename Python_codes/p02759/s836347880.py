import sys;input=lambda:sys.stdin.readline().rstrip();aint=lambda:int(input());ints=lambda:list(map(int,input().split()))
import math;floor,ceil=math.floor,math.ceil
from collections import deque
Yes=lambda b:print('Yes')if b else print('No');YES=lambda b:print('YES')if b else print('NO')
is_even=lambda x:True if x%2==0 else False

def main():
  n=aint()
  print(int(ceil(0.5*n)))
    
if __name__ == '__main__':
  main()