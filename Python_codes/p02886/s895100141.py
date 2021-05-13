from itertools import combinations

def mapt(fn, *args):
    return tuple(map(fn, *args))

n = int(input())
d = mapt(int, input().split(" "))

print(sum(d[a]*d[b] for a, b in combinations(range(n), 2)))