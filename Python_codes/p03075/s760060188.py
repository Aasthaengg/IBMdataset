*l,k=map(int,open(0).read().split())
from itertools import permutations 
perm = permutations(l, 2) 
ans=[]
for i in list(perm): 
  ans.append(i[1]-i[0])
print("Yay!" if max(ans)<= k else ":(")