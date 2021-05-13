from itertools import accumulate

n, x = map(int, input().split())
l = list(map(int, input().split()))
d = [0] + list(accumulate(l))
print(len([1 for e in d if e <= x]))
