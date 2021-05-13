inpl = lambda: list(map(int,input().split()))
L, R, d = inpl()
print(R//d - (L-1)//d)
