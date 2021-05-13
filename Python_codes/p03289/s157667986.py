S = input()

if S[0] == "A":
    if S.count("C") == 1:
        if S[2:-1].count("C") == 1:
            S = S.replace("A", "")
            S = S.replace("C", "")
            if S.islower():
                print("AC")
                exit()

print("WA")
