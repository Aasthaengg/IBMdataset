import itertools
def main():
  a,b = map(int,input().split())
  ans = False
  if a % 3 == 0:
    ans = True
  elif b % 3 == 0:
    ans = True
  elif (a + b) % 3 == 0:
    ans = True
  print("Possible" if ans else "Impossible")
if __name__ == '__main__':
  main()