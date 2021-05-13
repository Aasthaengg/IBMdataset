import itertools
def main():
  a,b = map(int,input().split())
  m = a+b
  m = max(m,a-b)
  m = max(m,a*b)
  print(m)
if __name__ == '__main__':
  main()