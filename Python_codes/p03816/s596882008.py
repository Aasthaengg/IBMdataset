from collections import Counter


n = int(input())
A = list(map(int, input().split()))

COUNTS = Counter(A)

x = sum(count - 1 for count in COUNTS.values())
if x % 2 == 1:
    x += 1

print(n - x)
