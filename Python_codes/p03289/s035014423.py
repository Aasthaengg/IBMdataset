S = list(input())

if S[0] != "A":
    print("WA")
elif S[2:-1].count("C") != 1:
    print("WA")
else:
    S.remove("A")
    S.remove("C")
    S = "".join(S)
    if S.islower():
        print("AC")
    else:
        print("WA")