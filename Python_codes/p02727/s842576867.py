(x,y,a,b,c),p,q,r=[[*map(int,i.split())]for i in open(0)]
print(sum(sorted(sorted(p)[-x:]+sorted(q)[-y:]+r)[-x-y:]))
