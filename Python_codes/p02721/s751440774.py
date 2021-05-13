N, K, C = map(int, input().split())
S = " " + input()

L = [0 for _ in range(K+1)]
R = [0 for _ in range(K+1)]

p = 1
i = 1
while i < N+1 and p <= K:
    if S[i] == "o":
        L[p] = i
        i += C
        p += 1
    i += 1

p = K
i = N
while i > 0 and p > 0:
    if S[i] == "o":
        R[p] = i
        i -= C
        p -= 1
    i -= 1

for i in range(1, K+1):
    if L[i] == R[i]:
        print(L[i])