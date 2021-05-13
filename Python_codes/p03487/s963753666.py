from collections import Counter

# input
N = int(input())
res = sum([c - n if c >= n else c for n, c in Counter(list(map(int, input().split()))).most_common()])

print(res)