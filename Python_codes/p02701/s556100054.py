from collections import Counter
N=int(input())
S=[input() for _ in [0]*N]
print(len(Counter(S).items()))