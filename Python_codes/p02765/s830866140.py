import math

def main():
  N, R = map(int, input().split())
  
  if N >= 10:
    print(R)
  else:
    print(int(100 * (10 - N)) + R)
  
  
  
main()