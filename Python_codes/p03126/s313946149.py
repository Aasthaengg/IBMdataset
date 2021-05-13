N,M  = (int(X) for X in input().split())
Food = set(range(1,M+1))
for T in range(0,N):
    Food = Food.intersection(set([int(X) for X in input().split()][1:]))
print(len(Food))