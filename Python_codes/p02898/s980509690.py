n,k,*h=map(int,open(0).read().split())
j=0
for i in range(n):
  if h[i]>=k:
    j+=1
print(j)