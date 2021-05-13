S = input()
if len(S) == 2:
    print(S)
else:
    S = list(S)
    S[0],S[1],S[2] = S[2],S[1],S[0]
    print("".join(S))
