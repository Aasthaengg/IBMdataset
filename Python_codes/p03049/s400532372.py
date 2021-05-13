_,*s=open(0).read().split()
a=b=c=d=0
for S in s:a+=S[-1]=='A';b+=S[0]=='B';c+=S[-1]+S[0]=='AB';d+=S.count('AB')
print(d+min(a,b)-(0<a==b==c))
