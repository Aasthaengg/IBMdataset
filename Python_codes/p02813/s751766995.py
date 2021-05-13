import itertools as it
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
a = 0
b = 0
array = list(it.permutations(i for i in range(1,N+1)))
for i,ar in enumerate(array):
    if ar == P:
        a = i
    if ar == Q:
        b = i
print(abs(a-b))