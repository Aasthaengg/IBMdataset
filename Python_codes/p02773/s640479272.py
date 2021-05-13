n=int(input())
dict={}
xs=[]
for i in range(n):
  s=input()
  xs+=[s]
  if s not in dict:
    dict[s]=1
  else:
    dict[s]+=1
pin=0
xs=list(set(xs))
for i in xs:
  pin=max(pin,dict[i])
ans=[]
for i in xs:
  if dict[i]==pin:
    ans+=[i]
ans.sort()
for i in ans:
  print(i)