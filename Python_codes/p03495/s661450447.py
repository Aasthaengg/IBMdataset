from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
AD = sorted(list(Counter(A).values()))
print(sum(AD[:len(AD) - k]))