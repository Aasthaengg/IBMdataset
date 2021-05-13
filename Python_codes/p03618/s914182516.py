from collections import Counter
A = input()

n = len(A)
c = Counter(A)
ans = n * (n-1) // 2 + 1
for value in c.values():
    dec = value * (value-1) // 2
    ans -= dec

print(ans)