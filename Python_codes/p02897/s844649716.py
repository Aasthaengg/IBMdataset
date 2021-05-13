import math
N = int(input())
mol = math.ceil(N/2) if N % 2 != 0 else N//2
print(mol/N)
