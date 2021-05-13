from functools import reduce
print("Odd" if reduce(lambda x,y: x*y, list(map(int, input().split())))&1 else "Even")