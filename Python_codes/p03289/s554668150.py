S = input()
if S[0] == "A":
    S_1 = S[1:]
    if S[2:-1].count("C") == 1:
        S_1 = S_1.replace("C", "", 1)
        if S_1.islower():
            print("AC")
            exit()
print("WA")