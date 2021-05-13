import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

x = [tuple(x) for x in itertools.permutations(range(1, N + 1), N)]
x.sort()
a = x.index(P)
b = x.index(Q)
ans = abs(a - b)
print(ans)