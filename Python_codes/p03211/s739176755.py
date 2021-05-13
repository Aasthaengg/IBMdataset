S = input()
mini = 1000
for i in range(len(S)-2):
    X = int(S[i] + S[i+1] + S[i+2])
    mini = min(abs(X-753), mini)
print(mini)