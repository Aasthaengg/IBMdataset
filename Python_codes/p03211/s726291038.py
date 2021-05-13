S = input()
N = len(S)
Anslist = []

for i in range(N-2):
    SS = abs(int(S[i:i+3]) - 753)
    Anslist.append(SS)

print(min(Anslist))