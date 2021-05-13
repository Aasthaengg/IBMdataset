x,*s=open(0)
h,w,k,*m=map(int,x.split())
for b in range(512):
 r=t=j=0;d=[0]*h
 while w-j:
  i=c=0
  while h-i:
   d[c]+=s[i][j]>'0';x=d[c]>k
   if(t<j)&x:r+=1;t=j;d=[0]*h;break
   r+=h*w*x;c+=b>>i&1;i+=1
  else:j+=1
 m+=r+bin(b).count('1'),
print(min(m))