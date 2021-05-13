import itertools
def main():
  X,t = map(int,input().split())
  print((X-t) if (X-t) >=0 else 0)
if __name__ == '__main__':
  main()