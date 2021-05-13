S = input()

if S[0] == "A":
    if S[2:-1].count("C") == 1:
        if S[1:].replace("C", "c").islower():
            print("AC")
            exit()

print("WA")

