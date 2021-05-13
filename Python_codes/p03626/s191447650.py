n,s,t=open(0)
a=3
for i in range(1,int(n)):
 if i<2or s[i-1]==t[i-1]:a*=2
 elif s[i-1]!=s[i]!=t[i]:a*=3
print(a%(10**9+7))