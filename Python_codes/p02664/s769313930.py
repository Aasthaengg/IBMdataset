def resolve():
    T = input()
    S = ""
    for i in range(len(T)):
        if T[i] == "D" or T[i] == "?":
            S += "D"
        else:
            S += "P"
    print(S)
resolve()