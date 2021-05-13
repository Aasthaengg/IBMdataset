from collections import Counter
L=sorted(Counter(map(int, open(0).read().split())).values())
print("YNEOS"[any(i!=j for i,j in zip(L,[1,1,2,2]))::2])