from collections import Counter
n = int(input())
d = [int(input()) for _ in range(n)]

print(len(Counter(d)))