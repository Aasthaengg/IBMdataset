import itertools
def main():
  a,b = map(int,input().split())
  mm = a
  if a > b:
    mm -=1
  print(mm)
if __name__ == '__main__':
  main()