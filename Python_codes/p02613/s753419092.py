from collections import Counter

N = int(input())

C = Counter()
for _ in range(N):
    C += {input(): 1}

for v in ["AC", "WA", "TLE", "RE"]:
    print(f"{v} x {C[v]}")