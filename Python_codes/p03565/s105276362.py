def main():
    S = list(input())
    T = input()
    judge = False
    lastidx = -1
    for i in range(len(S)-len(T)+1):
        judgetmp = True
        for j in range(len(T)):
            if S[i+j] != T[j] and S[i+j] != "?":
                judgetmp = False
                break
        if judgetmp:
            judge = True
            lastidx = i
    if not judge: return "UNRESTORABLE"
    for i in range(len(T)):
        S[lastidx+i] = T[i]
    return "".join(S).replace("?", "a")

print(main())
