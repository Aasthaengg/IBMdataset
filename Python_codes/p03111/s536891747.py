N,A,B,C = map(int,input().split())
l = []
for i in range(N):
  l.append(int(input()))
l.sort()

def tots(X, n):
    if (int(X/n)):
        return tots(int(X/n), n)+str(X%n)
    return str(X%n)

tnum = 0
ans = float("inf")
target = [A,B,C]
for i in range(4**N):
  #N本の竹の行き先の振り分け
  wake = [[],[],[],[]]
  ts = "0"*(N-len(tots(i,4)))+tots(i,4)
  for j in range(N):
    wake[int(ts[j])].append(l[j])
  if 0 == len(wake[0]) or 0 == len(wake[1]) or 0 == len(wake[2]):
    continue 
  #合成して行き先との長さの差をたしわせる
  c = 0
  for j in range(3):
    c +=abs(target[j] - sum(wake[j]))      
  tnum = len(wake[0])+len(wake[1])+len(wake[2])
  ans = min(ans,c+10*(tnum-3))  

if A in l and B in l and C in l:
  ans = 0
print(ans)  