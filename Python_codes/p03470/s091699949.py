import collections

n = int(input())
d = [int(input()) for i in range(n)]

ans = collections.Counter(d)
print(len(ans))