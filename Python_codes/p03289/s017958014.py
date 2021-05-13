def resolve():
    S = input()
    abc = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    if S[0]=="A":
        S = S[1:]
        if "C" in S[1:-1] and S.count("C")==1:
            S = S[:S.index("C")] + S[S.index("C")+1:]
            for i in range(len(S)):
                if S[i] in abc:
                    count += 1
            if count == len(S):
                print("AC")
            else:
                print("WA")
        else:
            print("WA")
    else:
        print("WA")
resolve()