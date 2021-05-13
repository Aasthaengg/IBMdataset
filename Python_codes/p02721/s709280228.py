n,k,c=map(int,input().split());s=input();
l=[];r=[];i=0;j=n-1
while 0<=i<=n-1:
  if s[i]=="o":l+=i,;i+=c+1
  else:i+=1
while 0<=j<=n-1:
  if s[j]=="o":r+=j,;j-=c+1
  else:j-=1
a=list(set(l)&set(r))
if len(a)>k:exit()
for q in sorted(a):print(q+1)