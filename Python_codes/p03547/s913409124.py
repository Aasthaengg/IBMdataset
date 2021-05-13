import itertools
def main():
  s1,s2 = map(str,input().split())
  if s1 < s2:
    ans = '<'
  elif s1 == s2:
    ans = '='
  else:
    ans = '>'
  print(ans)
if __name__ == '__main__':
  main()