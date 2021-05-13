from itertools import permutations
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

fac = 1
for i in range(1,N+1):
    fac *= i

n = [i+1 for i in range(N)]
ptr = sorted(list(permutations(n)))

p = 0
q = 0
for i in range(fac):
    if list(ptr[i]) == P:
        p = i
    if list(ptr[i]) == Q:
        q = i

print(abs(p-q))   