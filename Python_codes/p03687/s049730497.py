S = input()
N = len(S)
L = S
ans = 10000000
for c in set(S):
    S = L
    next = []
    while S.count(c) < len(S):
        for i in range(len(S)-1):
            if S[i+1] == c:
                next.append(S[i+1])
            else:
                next.append(S[i])
        S = next
        next = []
    ans = min(ans,N-len(S))
print(ans)