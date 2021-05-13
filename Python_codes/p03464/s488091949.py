_,a=open(0)
l,r=-2,-3
for a in map(int,a.split()[::-1]):l,r=l//a*a,r//a*a
print(-(l==r)or'%d %d'%(-l,~r))