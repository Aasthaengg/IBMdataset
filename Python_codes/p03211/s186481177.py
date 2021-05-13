#B - 754
S = list(map(int,input()))

minimam = 987
for i in range(len(S)-2):
    X = 100*S[i] + 10*S[(i+1)] + S[(i+2)]
    if abs(X - 753)<minimam:
        minimam = abs(X - 753)
print(minimam)