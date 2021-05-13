
S = input()
T = input()
if len(S) < len(T):
    print("UNRESTORABLE")
    exit(0)

for k in range(len(S)-len(T),-1,-1):
    f = 1
    for i in range(len(T)):
        if S[k+i] != "?":
            if S[k+i] != T[i]:
                f = 0
                break
    if f == 1:
        ans = ""
        for i in range(k):
            if S[i] == "?":
                ans += "a"
            else:
                ans += S[i]
        ans += T
        for i in range(k+len(T),len(S)):
            if S[i] == "?":
                ans += "a"
            else:
                ans += S[i]
        print(ans)
        exit(0)
print("UNRESTORABLE")
