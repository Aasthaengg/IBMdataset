N, Q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(Q)]
counters = [0 for _ in range(N + 1)]
for idx, s in enumerate(S):
    counters[idx + 1] = counters[idx] + (1 if S[idx:idx + 2] == "AC" else 0)
for q in queries:
    l, r = q
    print(counters[r - 1] - counters[l - 1])
