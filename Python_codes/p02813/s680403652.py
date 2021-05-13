import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

s = itertools.permutations(range(1, n+1))
l = []
for v in s:
    l.append(v)
p_index = l.index(p)
q_index = l.index(q)
print(abs(p_index - q_index))
