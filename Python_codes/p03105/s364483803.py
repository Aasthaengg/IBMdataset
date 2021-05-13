import sys
input = sys.stdin.readline

def main():
  A,B,C = [int(i) for i in input().strip().split()]
  return min(B//A,C)
  
if __name__ == "__main__":
  print(main())
  
