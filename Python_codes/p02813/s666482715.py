import itertools
n = int(input())
R = [i for i in range(1,n+1)]
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

i = 1
for r in itertools.permutations(R,n):
    if r == P:
        p = i
    if r == Q:
        q = i
    i += 1

print(abs(p-q))
