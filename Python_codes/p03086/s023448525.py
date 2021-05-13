T=input()
d=["A","T","G","C"]
ans=0
pre=0
for x in T:
  if x in d:
    pre+=1
  else:
    ans=(max(ans,pre))
    pre=0
print(max(ans,pre))