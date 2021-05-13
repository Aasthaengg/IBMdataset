s=input()
from collections import Counter
sc=Counter(s)
for a in sc:
    if sc[a]>(len(s)+2)//3:
        print("NO")
        exit()
print("YES")
