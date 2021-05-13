S = list(input().strip())
f = True
if S[0] == "A":
    S[0] = "a"
else:
    S[0] = "X"
if S[2:-1].count("C") == 1:
    S[S.index("C")] = "c"
else:
    S[0] = "X"
if "".join(S) == "".join(S).lower():
    print("AC")
else:
    print("WA")
