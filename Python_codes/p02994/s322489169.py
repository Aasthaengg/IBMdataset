N,L = (int(x) for x in input().split())
Apple = list(L-1+x for x in range(1,N+1))
Abs = list(abs(x) for x in Apple)
Remove = Abs.index(min(Abs))
del Apple[Remove]
print(sum(Apple))