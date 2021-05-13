n,*l=map(int,open(0).read().split())
c=[0]*13
for i in l: c[i//400]+=1
a=8-c[:8].count(0)
print(max(1,a),a+sum(c[8:]))