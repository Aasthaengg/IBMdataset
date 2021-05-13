n=int(input())
d={}
a=[]
for i in range(n):
  s=input()
  if s not in d:
    d[s]=1
    a.append(s)
  else:
    d[s]+=1
m=max(d.values())
a.sort()
for i in a:
  if d[i]==m:
    print(i)