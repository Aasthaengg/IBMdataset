import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

if P == Q:
    print(0)
    exit()

L = list(range(1, N+1, 1))

p = itertools.permutations(L, N)

cn = 0
cn1 = 0
cn2 = 0

for i in p:
    i = list(i)

    cn = cn + 1
    if i == P:
       cn1 = cn
    elif i == Q:
       cn2 = cn
       

print(abs(cn1 - cn2))