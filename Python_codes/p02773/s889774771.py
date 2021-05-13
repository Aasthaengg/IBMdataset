from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
S.sort()
s = Counter(S)
max_len = max([n for n in s.values()])
#print("------------------")
for a, b in s.items():
    if b == max_len:
        print(a)