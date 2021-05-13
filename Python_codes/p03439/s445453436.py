import sys

def q(i):
  print i
  sys.stdout.flush()
  s = raw_input()
  if s=="Vacant":
    sys.exit(0)
  else:
    return 0 if s=="Male" else 1

N, = map(int, raw_input().split())
S = [None]*N
l = 0
S[l] = q(l)
r = N-1
S[r] = q(r)
while True:
  m = (l+r)//2
  S[m] = q(m)
  if (m-l+S[m]-S[l])%2==0:
    l = m
  else:
    r = m