def resolve():
    S = input()
    c = 0
    f = 0
    C = []
    F = []
    for i in range(len(S)):
        if S[i] == "C":
            c = 1
            C.append(i)
        elif S[i] == "F":
            f = 1
            F.append(i)
    print("Yes" if c == 1 and f == 1 and min(C) < max(F) else "No")
resolve()