from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
S = Counter(S)
for s in ["AC", "WA", "TLE", "RE"]:
    print(f"{s} x {S[s]}")
