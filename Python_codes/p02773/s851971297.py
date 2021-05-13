n=int(input())
s={}
l=[]
for i in range(n):
  a=input()
  if a in s:
    s[a]+=1
  else:
    s[a]=1
    
cou=max(s.values())

for k,v in s.items():
  if v==cou:
    l.append(k)
    
ans=sorted(l)

for i in ans:
  print(i)