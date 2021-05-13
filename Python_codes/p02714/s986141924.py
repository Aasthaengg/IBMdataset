
N = int(input())
S = input()

d = {"R": 0, "G": 0, "B": 0}
for i in range(N):
    d[S[i]] += 1

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = 2 * j - i
        if k >= N:
            continue

        if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            cnt += 1

print(d["R"] * d["G"] * d["B"] - cnt)
