import itertools
def main():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  s1 = a
  s2 = c
  s1 = min(s1,b)
  s2 = min(s2,d)
  print(s1+s2)
if __name__ == '__main__':
  main()