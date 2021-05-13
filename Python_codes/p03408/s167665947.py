from collections import defaultdict

S = defaultdict(int)
T = defaultdict(int)

for _ in range(int(input())):
    S[input()] += 1

for _ in range(int(input())):
    T[input()] += 1

print(max(0, max([S[k] - T[k] for k, v in S.items()])))

