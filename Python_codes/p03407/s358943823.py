import sys
input = sys.stdin.readline

def main():
  A,B,C = map(int, input().split())
  if C <= A+B:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
  main()