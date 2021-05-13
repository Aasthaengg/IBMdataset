n,*s=open(0).read().split()
a=0;b=0;ba=0;ans=0
for s_i in s:
  b+=(s_i[0]=='B')*(not s_i[-1]=='A')
  a+=(not s_i[0]=='B')*(s_i[-1]=='A')
  ba+=(s_i[0]=='B')*(s_i[-1]=='A')
  ans+=s_i.count('AB')
print(ans+ba+min(a,b)-(ba>0)*(a+b==0))