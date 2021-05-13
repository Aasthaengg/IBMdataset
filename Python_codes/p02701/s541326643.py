from collections import Counter
N = int(input())

l = []

for _ in range(N):
    l.append(str(input()))
    
c = Counter(l)

print(len(c))