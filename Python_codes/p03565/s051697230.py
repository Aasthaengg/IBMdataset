S = input()
T = input()
for k in range(len(S)-len(T),-1,-1):
    f = 1
    for i in range(len(T)):
        if S[k+i] != "?" and S[k+i] != T[i]:
            f = 0
            break
    if f == 1:
        print(S[:k].replace("?","a")+T+S[k+len(T):].replace("?","a"))
        exit(0)
print("UNRESTORABLE")
