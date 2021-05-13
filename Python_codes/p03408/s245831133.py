import math
def main():
  n=int(input())
  s = [input() for i in range(n)]
  m=int(input())
  t = [input() for i in range(m)]
  ans=0
  while len(s)>0:
    num=s.count(s[0])-t.count(s[0])
    if ans<num:
      ans=num
    s=[x for x in s if x != s[0]]
  print(ans)
  
main()
