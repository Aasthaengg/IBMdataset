n=int(input())
l,r=0,n
print(0,flush=True)
s=input()
sl,sr=s,s
while True:
  m=(l+r)//2
  print(m,flush=True)
  sm=input()
  if (sm==sl)+((m-l)%2)==1:
    l=m
    sl=sm
  else:
    r=m
    sr=sm