#<B>
S = input()
S1 = S[0::2]
S2 = S[1::2]
ans1 = S1.count("R") + S1.count("U") + S1.count("D")
ans2 = S2.count("L") + S2.count("U") + S2.count("D")
if ans1 == len(S1) and ans2 == len(S2):
    print("Yes")
else:
    print("No")