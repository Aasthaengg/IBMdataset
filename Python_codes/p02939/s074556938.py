S = list(input())

c = 0
for i in range(1,len(S)):
    if S[i] == S[i-1]:
        c += 1
        if i+1 < len(S):
            S[i+1] = "0"

print(len(S)-c)