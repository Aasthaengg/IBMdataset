import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  for i in range(n):
    a = int(input())
    if a % 2 == 1:
      print('first')
      exit()
  print('second')
  
if __name__ == '__main__':
    main()