N = int(input())
S = [input() for _ in range(N)]

S = sorted(S)
newS = sorted(list(set(S)))
frq = [0] * len(newS)

si = index = 0
for i in range(N):
    if i == N-1:
        frq[index] = N - si
    elif S[i] != S[i+1]:
        frq[index] = i + 1 - si
        si = i + 1
        index += 1
    
ma = max(frq)
for i in range(len(newS)):
    if frq[i] == ma:
        print(newS[i])