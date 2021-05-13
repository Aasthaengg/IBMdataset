S = list(str(input()))
L = len(S)
if S[L-1] == "s":
    S.append("es")
else:
    S.append("s")
K =''.join(S)
print(K)