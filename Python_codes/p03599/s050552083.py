a,b,x,y,s,m = map(int,input().split())

#a,b,x,y,s,m = (1,2,1,2,100,1000)
a *= 100
b *= 100

#入れられる水の候補
waterlist=[]
amax = int(m/a)
for i in range(amax+1):
  bmax = int((m-a*i)/b)
  for j in range(bmax+1):
    water = a*i + b*j
    if water:
      waterlist.append(a*i + b*j)
waterlist = set(waterlist)

#砂糖の組み合わせから最大を
def makesatolist(maxsato,x,y):
  satolist = []
  xmax = int(maxsato/x)
  for i in range(xmax+1):
    ymax  = int((maxsato-x*i)/y)
    for j in range(ymax+1):
      satolist.append(x*i + y*j)
  return max(satolist)
  
nownodo = 0
ans = [0] * 2
for i in waterlist:
 
  # iグラムの水に何グラムの砂糖まで解ける？
  maxsato = i * s/100
  if i + maxsato > m:
    maxsato = m - i

  sato = makesatolist(maxsato,x,y)
  satowater = i + sato
  nodo = sato / satowater
  if nodo >= nownodo:
    nownodo = nodo
    ans = [satowater,sato]

print(ans[0]," ",ans[1])