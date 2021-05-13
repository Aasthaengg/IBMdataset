c=[int(i)for i in input().split()]
a=0
for i in range(3):
  if c[i]==sum([int(j)for j in c if j is not c[i]]):
  	a+=1
print("Yes" if a>0 else "No")