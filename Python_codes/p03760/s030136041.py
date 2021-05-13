O = input()
E = input()
for i in range(len(O)):
    print(O[i], end = "")
    if i+1 <= len(E):
        print(E[i], end = "")