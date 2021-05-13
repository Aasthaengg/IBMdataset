from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
c = Counter(arr)
arr = c.most_common()[k:]
print(sum([x[1] for x in arr]))