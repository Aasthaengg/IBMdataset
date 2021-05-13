import sys
input=sys.stdin.readline
import math

N,K=(int(x) for x in input().rstrip('\n').split())
R,S,P=(int(x) for x in input().rstrip('\n').split())
T = list(input().rstrip('\n'))
s_d = {'r':P,'s':R,'p':S}
score = 0
for i in range(K):
  now=i
  now_h=''
  while now<N:
    next= T[now]
    if next!=now_h:
      score += s_d[next]
      now_h=next
    else:
      now_h=''
    now += K
print(score)