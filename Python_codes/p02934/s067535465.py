def inpl(): return list(map(int, input().split()))
N = int(input())
print((1 / sum([1/a for a in inpl()])))