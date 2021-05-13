n,k,q=map(int,input().split())
p=[0]*n
for i in range(q):
  a=int(input())-1
  p[a]+=1
#print(p)
for i in p:
  print('Yes' if k-q+i>0 else 'No')