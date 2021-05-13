from collections import Counter
S = input()
C = Counter(S)
print((len(S)//2)+(C["p"]*(-1)))