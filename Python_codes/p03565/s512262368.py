S = list(input())
T = list(input())
import copy
ans = []
for i in reversed(range((len(S)-len(T))+1)):
    R = copy.deepcopy(S)
    for j in range(len(T)):
        if S[i+j] != "?" and S[i+j] != T[j]:
            break
    else:
        for j in range(len(T)):
            R[i+j] = T[j]
        for j in range(len(S)):
            R[j] = "a" if R[j] == "?" else R[j]
        ans.append("".join(R))
if ans:
    ans.sort()
    print(ans[0])
else:
    print("UNRESTORABLE")