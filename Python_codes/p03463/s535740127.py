def inpl(): return list(map(int, input().split()))
m, a, b = inpl()
print(['Alice','Borys'][(a+b)%2])