S = input()[::-1]
T = input()[::-1]

flag = False
for i in range(len(S) - len(T) + 1):
    matched = True

    for j in range(len(T)):
        # γγΌγ...
        if i == len(S) - len(T) + 1:
            break

        if S[i + j] != "?" and S[i + j] != T[j]:
            matched = False
    
    if matched:
        S = S[:i] + T + S[i + len(T):]
        flag = True
        break

if flag:
    print(S.replace("?", "a")[::-1])
else:
    print("UNRESTORABLE")