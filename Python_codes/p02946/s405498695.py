k,x=[int(s) for s in input().split()]

r=[]
for i in range(k-1):
  r.append(x-k+i+1)

for j in range(k):
  r.append(x+j)
  
print(*r)