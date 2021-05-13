N, C, *STC = map(int, open(0).read().split())

T = [[0] * 10 ** 5 for _ in range(C + 1)]
for s, t, c in zip(*[iter(STC)] * 3):
    T[c][s - 1:t] = [1] * (t - s + 1)

print(max(map(sum, zip(*T))))