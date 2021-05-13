def bikkuri(x):
  if x <= 0:
    return 1
  temp = 1
  for i in range(1,x+1):
    temp *= i
  return temp

def ncr(n,r):
  return bikkuri(n)//(bikkuri(r)*bikkuri(n-r))
  
#print(bikkuri(3))
#print(ncr(5,3))
from collections import defaultdict
dic = defaultdict(int)
N,A,B = map(int,input().split())
v = list(map(int,input().split()))
MAX = max(v)
for x in v:
  dic[x] += 1
ans = 0
w = sorted(v, reverse=True)
Maxv = [] #(sum,i個)を保存
for i in range(A,B+1): #A-Bまで
  #print(Maxv)
  dic2 = defaultdict(int)
  SUM = 0
  for j in range(i):
    dic2[w[j]] += 1
    SUM += w[j]
  L = list(dic2.keys())
  if len(Maxv) == 0 or Maxv[0][0]*i == SUM*Maxv[0][1]:
    Maxv.append((SUM,i))
    temp = 1
    nokori = i*1
    for x in L:
      if dic[x] >= nokori:
        temp *= ncr(dic[x],nokori)
        #print(dic[x],nokori,ncr(dic[x],nokori))
      elif dic[x] == dic2[x]:
        nokori -= dic[x]
      if nokori == 0:
        break
        
    ans += temp
  elif Maxv[0][0]*i < SUM*Maxv[0][1]:
    ans = 0
    Maxv = [(SUM,i)]
    temp = 1
    for x in L:
      if dic[x] != dic2[x]:
        temp *= ncr(dic[x],dic2[x])
        #print(temp,x,dic[x],dic2[x])
    ans += temp
#print(Maxv)
print(Maxv[0][0]/Maxv[0][1])
print(ans)
