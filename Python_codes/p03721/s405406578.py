N, K = list(map(int, input().split()))
C = [0]*(10**5+1)
S=set()
for _ in range(N):
    a, b = list(map(int, input().split()))
    C[a] += b
    S.add(a)

L = list(S)
L.sort()
i = 0
ct = C[L[0]]
while ct < K:
    i += 1
    ct += C[L[i]]
print(L[i])
