from collections import Counter
N=int(input())
B=[tuple(map(int, input().split())) for _ in range(N)]
R=[(x[0]-y[0],x[1]-y[1]) for x in B for y in B if x!=y]
C=Counter(R).most_common(1)
print(N-C[0][1] if C else N)
