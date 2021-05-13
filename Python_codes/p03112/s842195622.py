import sys
input = sys.stdin.readline
A,B,Q = map(int,input().split())
S = []
for i in range(A):
  temp = int(input())
  S.append(temp)
#S.sort()
T = []
for i in range(B):
  temp = int(input())
  T.append(temp)
#T.sort()
#print(S,T)

def jinja(x): #移動距離、神社の位置を出力
  if x <= S[0]:
    ret = [S[0]-x,0]
  elif x >= S[-1]:
    ret = [x-S[-1],A-1]
  else:
    ok = 0
    ng = A
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if S[mid] <= x:
        ok = mid
      else:
        ng = mid
    ret = [x - S[ok],ok,S[ng] - x,ng]
  return ret

def tera(x): #移動距離、神社の位置を出力
  if x <= T[0]:
    ret = [T[0]-x,0]
  elif x >= T[-1]:
    ret = [x-T[-1],B-1]
  else:
    ok = 0
    ng = B
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if T[mid] <= x:
        ok = mid
      else:
        ng = mid
    ret = [x - T[ok],ok,T[ng] - x,ng]
  return ret
      

#P = tera(100)
#print(P)
for i in range(Q):
  INPUT = int(input())
  j = jinja(INPUT)
  #print(j)
  if len(j) == 2:
    x = j[0]; loc = S[j[1]]
    jt = tera(loc)
    if len(jt) == 2:
      x += jt[0]
    else:
      x += min(jt[0],jt[2])
  else:
    x1 = j[0]; loc1 = S[j[1]]; x2 = j[2]; loc2 = S[j[3]]
    jt1 = tera(loc1); jt2 = tera(loc2)
    if len(jt1) == 2:
      x1 += jt1[0]
    else:
      x1 += min(jt1[0],jt1[2])
    if len(jt2) == 2:
      x2 += jt2[0]
    else:
      x2 += min(jt2[0],jt2[2])
    x = min(x1, x2)
  t = tera(INPUT)
  #print(t)
  if len(t) == 2:
    y = t[0]; loc = T[t[1]]
    tj = jinja(loc)
    #print(y,loc,tj)
    if len(tj) == 2:
      y += tj[0]
    else:
      y += min(tj[0],tj[2])
  else:
    y1 = t[0]; loc1 = T[t[1]]; y2 = t[2]; loc2 = T[t[3]]
    tj1 = jinja(loc1); tj2 = jinja(loc2)
    if len(tj1) == 2:
      y1 += tj1[0]
    else:
      y1 += min(tj1[0],tj1[2])
    if len(tj2) == 2:
      y2 += tj2[0]
    else:
      y2 += min(tj2[0],tj2[2])
    y = min(y1, y2)
  #print(x,y)
  print(min(x,y))