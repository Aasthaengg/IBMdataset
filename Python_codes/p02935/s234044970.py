from functools import reduce
N = int(input())
V = sorted(list(map(int, input().split())))
print(reduce(lambda x,y: (x+y)/2, V))