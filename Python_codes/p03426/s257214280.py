h,w,d=map(int,input().split())
a=[]
adic={}
hh=1
saidai=0
for _ in range(h):
  temp=(list(map(int,input().split())))
  ww=1
  for item in temp:
    adic[item]=[hh,ww]
    ww+=1
    saidai=max(saidai,item)
  
  hh+=1
  
rdic={}
#print("saidai",saidai)
i=1
    

while i<=d:

  rdic[i]=0
  hoge=i+d
  while hoge<=saidai:
    tempi=adic[hoge-d]
    tempd=adic[hoge]
    rdic[hoge]=rdic[hoge-d]+abs(tempi[0]-tempd[0])+abs(tempi[1]-tempd[1])
    hoge+=d
  i+=1
#print(rdic)

q=int(input())
rl=[]
for _ in range(q):
  rl.append(list(map(int,input().split())))
  
for item in rl:
  print(rdic[item[1]]-rdic[item[0]])