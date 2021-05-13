import sys
input = sys.stdin.readline

def main():
  n = int(input())
  for _ in range(n):
    a = int(input())
    if a%2:
      print("first")
      break
  else:
    print("second")
    
if __name__ == '__main__':
  main()