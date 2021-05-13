def resolve():
    S = input()
    a = []
    z = []
    for i in range(len(S)):
        if S[i] == "A":
            a.append(i)
        elif S[i] == "Z":
            z.append(i)
    print(z[-1]-a[0]+1)
resolve()