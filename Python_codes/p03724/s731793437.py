from collections import Counter as C
N,M,*A=map(int, open(0).read().split())
print("YNEOS"[any(a&1 for a in C(A).values())::2])