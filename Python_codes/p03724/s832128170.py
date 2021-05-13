n,m,*p=map(int,open(0).read().split());c=[0]*n
for x in p:c[x-1]+=1
print("YNEOS"[any(x%2for x in c)::2])