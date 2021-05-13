n=int(input())
a=list(map(lambda x:1 if "#"==x else 0,list(input())))
mn=n-sum(a)
s=mn
for i in a:
  if i:
    s+=1
  else:
    s-=1
  mn=min(mn,s)
print(mn)