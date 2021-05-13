S = input().rstrip()
D = [[-1] for _ in range(26)]
E = [[0] for _ in range(26)]
for i, s in enumerate(S):
    E[ord(s)-ord("a")].append(i-D[ord(s)-ord("a")][-1]-1)
    D[ord(s)-ord("a")].append(i)
for i in range(26):
    E[i].append(len(S)-1-D[i][-1])
res = []
for i in range(26):
    res.append(max(E[i]))
print(min(res))

