N = int(input())
L = sorted([list(input().split()) + [i + 1] for i in range(N)], key = lambda x: x[0])
while len(L) > 0:
    c = sum([x[0] == L[0][0] for x in L])
    M = sorted(L[0: c], key = lambda x : int(x[1]), reverse = True)
    for x in M:
        print(x[2])
    L = L[c:]