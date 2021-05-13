S=input()
if S[0]=="A" and S[2:-1].count("C")==1 and S[1].islower() and S[-1].islower():
    for s in S[2:]:
        if s!="C":
            if s.islower():
                print("AC")
                exit()
print("WA")

