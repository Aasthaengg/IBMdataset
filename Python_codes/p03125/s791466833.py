def main():
  #n = int(input())
  #s = input()
  #s = input().split()
  a,b = list(map(int,input().split()))
  #a = [input() for i in range(n)]
  #a = [int(input()) for i in range(n)]
  #a = [input().split() for i in range(n)]
  #a = [list(map(int,input().split())) for i in range(n)]
  ans = 0
  count = 0
  lis = []
  
  if b%a == 0:
    print(a+b)
  else:
    print(b-a)

if __name__ == '__main__':
  main()