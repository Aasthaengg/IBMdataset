from collections import*
n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in a[1:]:
  ans^=i
a=dict(Counter(a))
ak=list(a.keys())
if len(a)==1 and ak[0]!=0:ans=1
elif len(a)==2 and a.get(0)!=n//3:ans=1
elif len(a)==3 and not(a[ak[0]]==a[ak[1]]==a[ak[2]]==n//3):ans=1
elif len(a)>3:ans=1
print(['Yes','No'][ans>0])