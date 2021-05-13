from collections import Counter

N = input()
n = len(N)

NC = Counter(N)
ans = n * (n - 1) // 2 + 1

for value in NC.values():
    ans -= value * (value - 1) // 2

print(ans)