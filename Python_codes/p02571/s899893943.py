S = input()
T = input()
n = len(T)
ans = len(T)
for st in range(0, len(S)-len(T)+1):
    SS = S[st:st+len(T)]
    tmp = len(T)
    for s,t in zip(SS,T):
        if s==t:
            tmp -= 1
    ans = min(ans, tmp)
print(ans)
