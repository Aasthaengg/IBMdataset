S = input()
T = input()
s,t = len(S),len(T)
for i in range(s-t,-1,-1):
    for j in range(t):
        if S[i+j] != T[j] and S[i+j] != "?":
            break
    else: 
        S = S[:i] + T + S[i+t:]
        break
else:
    print("UNRESTORABLE")
    exit()

S = list(S)
for i in range(s):
    if S[i] == "?":
        S[i] = "a"
print(*S, sep = "")