from functools import reduce

f = lambda a,b: "a > b" if a > b else "a < b" if a < b else "a == b"

print(reduce(f, map(int, input().split())))