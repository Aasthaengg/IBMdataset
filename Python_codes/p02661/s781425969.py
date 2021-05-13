from statistics import median
N=int(input())
a,b=[],[]
#print(map(int,input().split())
for i in range(N):
  i,j=map(int,input().split())
  a.append(i)
  b.append(j)
amed,bmed=median(a),median(b)
  
if N%2==1:
  print(int(bmed-amed+1))
else:
  print(int(2*(bmed-amed)+1))