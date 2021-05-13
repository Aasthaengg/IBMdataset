def resolve():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        if S.count("A") == 1 and S.count("C") == 1:
            S = S.replace("A", "").replace("C", "")
            if S == S.lower():
                print("AC")
                return
    print("WA")


resolve()
