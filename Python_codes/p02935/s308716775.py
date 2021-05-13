_,l=open(0)
l=sorted(map(int,l.split()))
v=l[0]
for i in l: v=(v+i)/2
print(v)