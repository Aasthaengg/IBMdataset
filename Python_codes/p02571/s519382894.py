##B - Substring
S = str(input())
T = str(input())
L = len(S) - len(T) + 1
##print(L)
ansL = []
for i in range(L):
    ans = 0
    for j in range(len(T)):
        if S[j] != T[j]:
            ans += 1
    ##print(ans)
    ansL.append(ans)
    S = S[1:]
print(min(ansL))