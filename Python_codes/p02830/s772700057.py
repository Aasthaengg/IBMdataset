N,S,T = open(0).read().split()
print(''.join([''.join(s) for s in zip(S,T)]))