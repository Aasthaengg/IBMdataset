N = int(input())
A = [int(_) for _ in input().split()]

O, E = [], []

for i, a in enumerate(A):
    if a % 2 == 0:
        o, e = 2, 1
    else:
        o, e = 1, 2
        
    if i == 0:
        O.append(o)
        E.append(e)
    else:           
        numo, nume = 0, 0
        numo += O[-1] * o
        nume += E[-1] * e
        nume += E[-1] * o
        nume += O[-1] * e

        O.append(numo)
        E.append(nume)

print(E[-1])
