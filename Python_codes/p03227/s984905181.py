S = str(input())

if len(S) == 3:
    Sarray = []
    for i in range(3):
        Sarray.append(list(S)[2 - i])
    S = ''
    for i in range(3):
        S += Sarray[i]

print(S)