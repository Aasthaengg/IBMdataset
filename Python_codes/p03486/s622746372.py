import math
def main():
  s = input()
  t = input()
  sx=sorted(s)
  tx=sorted(t,reverse=True)
  if sx<tx:
    print('Yes')
  else:
    print('No')
main()
