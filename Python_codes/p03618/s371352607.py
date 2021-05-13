from collections import Counter
a = input()
n = len(a)
cnt = Counter(a)
print(n * (n - 1) // 2 - sum(v * (v - 1) // 2 for k, v in cnt.items()) + 1)