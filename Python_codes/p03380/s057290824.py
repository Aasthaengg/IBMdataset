n=int(input())
l=list(map(int,input().split()))
m=max(l)
l.remove(m)
if m%2!=0:
  med=(m+1)//2
else:
  med=m//2
mi=m
for ll in l:
  mi=min(mi,abs(ll-med))
if med+mi in l:
  print(m,med+mi)
else:
  print(m,med-mi)