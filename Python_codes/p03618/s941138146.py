from collections import Counter
s = input()
n = len(s)
print(n * ~-n // 2 + 1 - sum(i * ~-i // 2 for i in Counter(s).values()))