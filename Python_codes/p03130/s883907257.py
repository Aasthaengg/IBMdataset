import sys
import itertools

abset=set()
for _ in range(3):
  a,b=map(int,input().split())
  abset.add((a,b))
#print(abset)

for perm in itertools.permutations(range(1,5)):
  #print(perm)
  
  for i in range(1,4):
    if not (perm[i-1],perm[i]) in abset and not (perm[i],perm[i-1]) in abset:
      break
  else:
    #print(perm)
    print("YES")
    sys.exit(0)
else:
  print("NO")