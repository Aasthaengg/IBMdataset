def solver(N,S):
    ACs = S.count("AC")
    WAs = S.count("WA")
    TLEs = S.count("TLE")
    REs = S.count("RE")
    print("AC x",ACs)
    print("WA x",WAs)
    print("TLE x",TLEs)
    print("RE x",REs)

N = int(input())
S = []
for i in [0] * N:
    S.append(input())
solver(N,S)