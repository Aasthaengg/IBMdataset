n,*p=map(int,open(0))
s=[0]*-~n
for i in p:s[i]=s[i-1]+1
print(n-max(s))