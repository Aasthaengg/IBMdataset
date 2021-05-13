S = list(input())
for x in range(len(S)):
    if S[x] == "1":
        S[x] = "9"
    elif S[x] == "9":
        S[x] = "1"
print("".join(S))
