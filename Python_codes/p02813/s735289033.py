import itertools

n = int(input())
a = [i for i in range(1,n+1)]
b = list(itertools.permutations(a))
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
pi = b.index(p)
qi = b.index(q)

print(abs(pi - qi))