S = input()

cnt = 0
i = 0
while i < (len(S)-1):
    if S[i] == S[i+1]:
        cnt += 1
        i += 3
    else:
        i += 1

print(len(S) - cnt)
