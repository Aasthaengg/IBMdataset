S = input()

if S[0] == S[1] == S[2] == "R":
    print(3)

elif (S[0] == S[1] == "R" and S[2] == "S") or (S[1] == S[2] == "R" and S[0] == "S"):
    print(2)

elif "R" in S:
    print(1)

else:
    print(0)