import sys
def g(i):
  print i
  sys.stdout.flush()
  s = raw_input()
  if s=="Vacant":
    sys.exit(0)
  return 0 if s=="Male" else 1

N = int(raw_input())
S = [0]*N
l = 0
S[l] = g(l)
r = N-1
S[r] = g(r)
while True:
  c=(r+l)//2
  S[c]=g(c)
  if (c-l)%2==(S[c]+S[l])%2:
    l=c
  else:
    r=c