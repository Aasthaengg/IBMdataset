from collections import Counter
N = int(input())
L = ["".join(sorted(input())) for _ in range(N)]
T = Counter(L).values()
print(sum(v*(v-1)//2 for v in T))