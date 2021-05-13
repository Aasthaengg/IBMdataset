import itertools
def main():
  a,b,c,d = map(int,input().split())
  ans = False
  if abs(c-a) <= d:
    ans = True
  elif abs(a-b) <= d and abs(b-c) <= d:
    ans = True
  else:
    ans = False
#  print("Yes" if abs(c-a) <= d else"No")
  print("Yes" if ans else "No")
if __name__ == '__main__':
  main()