from collections import defaultdict

n = int(input())
d = [int(input()) for i in range(n)]

dict = defaultdict(int)
for i in d:
    dict[i] += 1
print(len(dict))
