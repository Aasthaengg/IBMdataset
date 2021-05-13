from collections import Counter


A = input()
N = len(A)
cntr = Counter(A)
ans = 0
for c in A:
    ans += N - cntr[c]
ans //= 2
print(ans + 1)
