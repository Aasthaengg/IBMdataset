import itertools
import sys
s=input()
for i in itertools.product(["A",""],repeat=4):
  if i[0]+"KIH"+i[1]+"B"+i[2]+"R"+i[3]==s:
    print("YES")
    sys.exit()
    
print("NO")
