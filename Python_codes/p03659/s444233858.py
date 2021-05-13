from itertools import accumulate

input()
a = list(map(int, input().split()))
b = list(accumulate(a))
print(min([abs(y * 2 - b[-1]) for y in b][:-1]))