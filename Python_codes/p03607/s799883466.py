from collections import Counter
N = int(input())
c = Counter([input() for _ in range(N)])
print(sum(i%2 for i in c.values()))