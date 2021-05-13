import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from bisect import bisect

a,b,q = map(int,readline().split())
s = [int(readline()) for i in range(a)]
t = [int(readline()) for i in range(b)]

for i in range(q):
  x = int(input())
  ss = bisect(s,x)
  if ss == 0:
    sR = s[0]
    sL = s[0]
  elif ss == len(s):
    sR = s[-1]
    sL = s[-1]
  else:
    sR = s[ss]
    sL = s[ss-1]
    
  sRt = bisect(t,sR)
  sLt = bisect(t,sL)
  if sRt == 0:
    sRtL = t[0]
  else:
    sRtL = t[sRt-1]
  if sLt == len(t):
    sLtR = t[-1]
  else:
    sLtR = t[sLt]
  if sRt == len(t):
    sRtR = t[-1]
  else:
    sRtR = t[sRt]
  if sLt == 0:
    sLtL = t[0]
  else:
    sLtL = t[sLt-1]
  chk = min(abs(x-sL)+abs(sL-sLtL),abs(x-sL)+abs(sL-sLtR),abs(x-sR)+abs(sR-sRtR),abs(x-sR)+abs(sR-sRtL))
  ss = bisect(t,x)
  if ss == 0:
    sR = t[0]
    sL = t[0]
  elif ss == len(t):
    sR = t[-1]
    sL = t[-1]
  else:
    sR = t[ss]
    sL = t[ss-1]
  sRt = bisect(s,sR)
  sLt = bisect(s,sL)
  if sRt == 0:
    sRtL = s[0]
  else:
    sRtL = s[sRt-1]
  if sLt == len(s):
    sLtR = s[-1]
  else:
    sLtR = s[sLt]
  if sRt == len(s):
    sRtR = s[-1]
  else:
    sRtR = s[sRt]
  if sLt == 0:
    sLtL = s[0]
  else:
    sLtL = s[sLt-1]  
  chk = min(chk,abs(x-sL)+abs(sL-sLtL),abs(x-sL)+abs(sL-sLtR),abs(x-sR)+abs(sR-sRtR),abs(x-sR)+abs(sR-sRtL))
  print(chk)