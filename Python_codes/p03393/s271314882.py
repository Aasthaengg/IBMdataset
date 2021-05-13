S = input()
alpha = list("abcdefghijklmnopqrstuvwxyz")

if len(S) < 26:
    s = set(list(S))
    for i in range(26):
        if alpha[i] not in s:
            S += alpha[i]
            break
else:
    flag = False
    for i in range(24, -1, -1):
        tmp = ord(S[i])
        for j in range(25, i, -1):
            if tmp < ord(S[j]):
                S = S[:i] + S[j]
                flag = True
                break    
        
        if flag:
            break
    else:
        S = "-1"

print(S)