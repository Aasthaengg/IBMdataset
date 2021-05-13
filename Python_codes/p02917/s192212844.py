n,*l=map(int,open(0).read().split())
s,p=0,l[0]
for i in l: s+=min(p,i); p=i
print(s+p)