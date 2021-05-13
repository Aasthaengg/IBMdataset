n, m, x = map(int, input().split())
a = list(map(int, input().split()))
print(min(sum([1 for i in a if i>x]),sum([1 for i in a if i<x])))