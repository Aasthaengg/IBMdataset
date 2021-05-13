S = input()

if S[0] == "A" and S.count("A") == 1 and S.count("C") == 1:
    p = S.find("C")
    b = S.replace("A","").replace("C","")
    if p > 1 and p < len(S) - 1 and b.islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")
