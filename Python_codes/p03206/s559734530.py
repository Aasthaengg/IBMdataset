import itertools
import fractions
def main():
  d = int(input())
  if d == 25:
    ans = "Christmas"
  elif d == 24:
    ans = "Christmas Eve"
  elif d == 23:
    ans = "Christmas Eve Eve"
  elif d == 22:
    ans = "Christmas Eve Eve Eve"
  
  print(ans)
if __name__ == '__main__':
  main()