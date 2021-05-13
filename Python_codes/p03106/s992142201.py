a,b,k=map(int,input().split())

Min=min(a,b)

l=[]

for i in range(Min,0,-1):
  if a%i==0 and b%i==0:
    l.append(i)

#print(l)

print(l[k-1])