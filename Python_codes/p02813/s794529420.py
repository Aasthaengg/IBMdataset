import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

a,b = 0,0
for i, perm in enumerate(itertools.permutations(range(1, N+1)), 1):
    if P==perm:
        a = i
    if Q==perm:
        b = i
    if a > 0 and b > 0:
        print(abs(a-b))
        exit()