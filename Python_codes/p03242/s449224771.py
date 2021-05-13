S = input()
N = len(S)
T = ""
for i in range(N):
    if S[i] == "1":
        T += "9"
    elif S[i] == "9":
        T += "1"
    else:
        T += S[i]
print(int(T))
