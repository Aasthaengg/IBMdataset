N = int(input())
V = sorted([int(x) for x in input().split()])
Fus = (V[0]+V[1])/2
for T in range(2,N):
    Fus = (Fus+V[T])/2
print(Fus)