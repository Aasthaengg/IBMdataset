from collections import Counter

n = int(input())
a = list(map(int, input().split()))
freq = Counter(a)
ordering = []
for i in range(n):
    right = n - i - 1
    left = i
    ordering.append(abs(right - left))
freq2 = Counter(ordering)
if freq != freq2:
    print(0)
else:
    result = 1
    for x in freq.values():
        result *= x
    print(result % (10 ** 9 + 7))