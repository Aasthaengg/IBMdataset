from collections import Counter

A = list(input())
a = len(A)
A = Counter(A)
answer = a * (a - 1) // 2 + 1
for i in A.values():
    answer -= i * (i - 1) // 2

print(answer)