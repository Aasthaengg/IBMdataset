def main():
  n = int(input())
  #s = input()
  #s = input().split()
  #a,b = list(map(int,input().split()))
  #a = [input() for i in range(n)]
  #a = [int(input()) for i in range(n)]
  #a = [input().split() for i in range(n)]
  #a = [list(map(int,input().split())) for i in range(n)]
  ans = 0
  count = 0
  lis = []
  
  if n == 25:
    print("Christmas")
  elif n == 24:
    print("Christmas Eve")
  elif n == 23:
    print("Christmas Eve Eve")
  else:
    print("Christmas Eve Eve Eve")
if __name__ == '__main__':
  main()