for s in iter(input,'-'):
 for _ in[0]*int(input()):
  n=int(input())
  s=s[n:]+s[:n]
 print(s)
