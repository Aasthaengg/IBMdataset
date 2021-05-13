S = input()
N = len(S)

p = [i + (1 if S[i] == "R" else -1) for i in range(N)]
i = 1
while i < N:
    p = [p[p[j]] for j in range(N)]
    i <<= 1
ans = [0] * N
for i in range(N):
    ans[p[i]] += 1
print(" ".join(map(str, ans)))