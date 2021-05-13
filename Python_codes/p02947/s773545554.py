from collections import Counter
N = int(input())
C = Counter(["".join(sorted(input())) for n in range(N)])
print(sum(n*(n-1)//2 for n in C.values()))