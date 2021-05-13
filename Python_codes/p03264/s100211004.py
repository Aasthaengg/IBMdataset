import itertools 
k=int(input());ans=0
l=list(itertools.combinations([i for i in range(1,k+1)], 2));
for i in l:
  if (i[0]%2!=0 and i[1]%2==0) or (i[0]%2==0 and i[1]%2!=0):ans+=1
print(ans)