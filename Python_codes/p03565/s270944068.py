S = input()
T = input()
if len(S)<len(T):
    print("UNRESTORABLE")
else:
    lenS =len(S)
    lenT = len(T)
    for i in range(lenS-lenT+1):
        if S[lenS-1-i] == "?" or S[lenS-1-i] == T[lenT-1]:
            for j in range(lenT):
                if S[lenS-1-i-j] != T[lenT-1-j] and S[lenS-1-i-j] != "?":
                    flag = 0
                    break
                flag = 1
            if flag == 1:
                for j in range(lenT):
                    S = S[:(lenS-1-i-j)]+T[lenT-1-j]+S[(lenS-i-j):]
                    #S[lenS-1-i-j] = T[lenT-1-j]
                for k in range(lenS):
                    if S[k] == "?":
                        print("a",end="")
                    else:
                        print(S[k],end="")
                print("")
                break
    else:
        print("UNRESTORABLE")