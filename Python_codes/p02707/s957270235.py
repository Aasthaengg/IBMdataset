from collections import Counter

n = int(input())
s = map(int, input().split(" "))
data = Counter(s)
for i in range(1, n+1):
    print(data.get(i, 0))