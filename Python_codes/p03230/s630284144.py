n = int(input())

k = 0
for i in range(1, 2*n+1):
    if i*(i-1) == 2*n:
        k = i

#print(k)
if not k:
    print('No')
    exit()

S = [[] for _ in range(k)]
import itertools
C = list(itertools.combinations(range(k),2))
for i in range(n):
    j = i+1
    c1, c2 = C[i]
    S[c1].append(j)
    S[c2].append(j)

print('Yes')
print(k)
for i in range(k):
    print(len(S[i]), *S[i])
