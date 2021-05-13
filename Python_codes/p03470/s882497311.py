from collections import Counter
N = int(input())
d = [int(input()) for i in range(N)]
d = Counter(d)
print(len(d))
