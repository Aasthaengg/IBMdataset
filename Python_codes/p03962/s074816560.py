import collections

a = list(input().split())
ans = len(collections.Counter(a))
print(ans)