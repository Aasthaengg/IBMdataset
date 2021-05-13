S = input()
t = 1000
for s in range(len(S)-2):
    t = min(abs(753 - int(S[s:s+3])),t)
print(t)