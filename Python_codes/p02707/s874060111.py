from collections import Counter
N = int(input())
d = Counter(map(int, input().split()))
for i in range(1, N+1):
    print(d[i])
