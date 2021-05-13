S = input()
ans = 0
for i in range(len(S)):
    for j in range(len(S)-i):
        ACGT = True
        for k in range(len(S)-i-j):
            if S[i:len(S)-j][k] != 'A' and S[i:len(S)-j][k] != 'G' and S[i:len(S)-j][k] != 'C' and S[i:len(S)-j][k] != 'T':
                ACGT = False
                break
        if ACGT and len(S)-i-j > ans:
            ans = len(S)-i-j
print(ans)
