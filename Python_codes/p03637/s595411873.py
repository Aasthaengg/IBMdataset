n=int(input())
la=list(map(int,input().split()))
lc=[0]*n
for i in range(n):
  t=la[i]
  while t%2<1 and lc[i]<2:
    t//=2; lc[i]+=1
c=[lc.count(i) for i in range(3)]
print('YNeos'[c[0]-c[2]>1 or (c[0]>c[2] 
and n%2<1)::2])