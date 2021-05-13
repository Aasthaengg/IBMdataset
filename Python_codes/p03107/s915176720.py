from collections import Counter

S = list(input())

count = Counter(S)
n = min(count['0'], count['1'])
print(n * 2)

