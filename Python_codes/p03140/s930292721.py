n=int(input())
a=input()
b=input()
c=input()
ans=0
for i in range(n):
  aa,bb,cc=a[i],b[i],c[i]
  if aa==bb:
    if cc!=aa:
      ans+=1
  else:
    if cc!=aa and cc!=bb:
      ans+=2
    else:
      ans+=1
print(ans)