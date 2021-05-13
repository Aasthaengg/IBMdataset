S = input()
if S[0] == "A":
    if (S.count("C") == 1) and (S[2:-1].count("C")==1):
        S = S[1:].replace("C", "")
        if S.islower():
            print("AC")
            exit(0)

print("WA")