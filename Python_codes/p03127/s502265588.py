n=int(input()) 
lis=list(map(int,input().split()))
m=min(lis)
new=lis
num=0
while True:
  for i in range(n+num):
    new[i]%=m
  if all(nn==0 for nn in new):
    print(m)
    exit()
  new.append(m)
  sl={m}
  for i in range(n+num):
    if new[i]!=0:
      sl.add(new[i])
  m=min(sl)
  num+=1