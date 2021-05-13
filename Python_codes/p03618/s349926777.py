from collections import Counter
A = input()
n = len(A)-1
ans = int(n*(n+1) // 2) + 1
count_a = Counter(A)
for c in count_a.values():
    ans -= ((c * (c-1)) // 2)
print(ans)