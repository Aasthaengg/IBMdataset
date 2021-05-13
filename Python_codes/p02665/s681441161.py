*a,=map(int,[*open(0)][1].split())
c=sum(a)
s=b=1
for a in a:c-=a;b=min(c,b-a<<1);s+=b
print(max(-1,s))