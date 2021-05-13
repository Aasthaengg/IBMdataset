S = list(str(input()))
t = 0
for i in range(len(S)):
    if S[i] != S[len(S)-1-i]:
        S[len(S)-1-i]=S[i]
        t +=1
print(t)