from itertools import accumulate

input()
a = list(map(int, input().split()))
b = list(accumulate(a))
c = [abs(y * 2 - b[-1]) for y in b][:-1]
print(min([abs(y * 2 - b[-1]) for y in b][:-1]))