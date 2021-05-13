O = input()
E = input()
if len(O) == len(E):
    for i in range(len(O)):
        print(O[i], end="")
        print(E[i], end="")
elif len(O) > len(E):
    for i in range(len(E)):
        print(O[i], end="")
        print(E[i], end="")
    print(O[i+1])
else:
    for i in range(len(E)):
        print(O[i], end="")
        print(E[i], end="")
    print(E[i+1])