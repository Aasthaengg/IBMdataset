N, *A = open(0).read().split()
A = sorted((s, -int(p), i) for i, (s, p) in enumerate(zip(*[iter(A)]*2)))
print('\n'.join(map(str, (x[2]+1 for x in A))))
