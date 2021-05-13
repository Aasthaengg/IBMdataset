# input
D = int(input())

C = "Christmas"
E = " Eve"
if D == 24:
    C += E 
elif D == 23:
    C += E * 2
elif D == 22:
    C += E * 3

print(C)