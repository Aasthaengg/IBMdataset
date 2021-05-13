D = {}
D["A"] = input()
D["B"] = input()
D["C"] = input()

t = "A"
while 1:
    if len(D[t]) == 0:
        winner = t
        break
    if D[t][0] == "a":
        u = "A"
    elif D[t][0] == "b":
        u = "B"
    elif D[t][0] == "c":
        u = "C"
    D[t] = D[t][1:]
    t = u
print(winner)
