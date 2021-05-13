import collections
n=int(input())
s=[]
for i in range(n):
  c=input()
  s.append(c)
a=collections.Counter(s)
d=sorted(a.items(), key=lambda x:x[1])
e=max(a.values())
l=[]
for i in a:
  if a[i]==e:
    l.append(i)
l.sort()
for i in l:
  print(i)