N = int(input())
C = str(input())
white = C.count('W')
Ccut = C[N-white:]
print(Ccut.count('R'))