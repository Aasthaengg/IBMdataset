from itertools import permutations 
perm = permutations(map(int,input().split()), 2) 
ans=[]
for i in list(perm): 
  ans.append(sum(i))
print(min(ans))