
N, Q = map(int, input().split())
S = input()

n = len(S)
ctr = [0] * n
for i in range(n):
    if i > 0 and S[i - 1] == "A" and S[i] == "C":
        ctr[i] = 1

cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + ctr[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l - 1] - ctr[l - 1])
