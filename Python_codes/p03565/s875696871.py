s = input()
T = input()
n_s = len(s)
n_t = len(T)
S = ""
for i in range(n_s-n_t+1):
    s_i = s[i:n_t+i]
    flag = True
    for j in range(n_t):
        if s_i[j] != "?":
            if s_i[j] != T[j]:
                break
    else:
        S = s[:i] + T + s[n_t+i:]
#print(S)
if S == "":
    print("UNRESTORABLE")
    exit()
    
S = list(S)
for i in range(n_s):
    if S[i] == "?":
        S[i] = "a"
print("".join(S))
