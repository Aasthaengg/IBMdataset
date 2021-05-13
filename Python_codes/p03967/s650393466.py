s=input()
from collections import Counter
lens=len(s)%2
s=Counter(s)
print(((s["g"]-s["p"])-lens)//2)