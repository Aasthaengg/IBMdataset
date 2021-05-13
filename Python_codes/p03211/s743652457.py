S = input()
T = 753
Z = []
for i in range(len(S)):
    Z.append(abs(int(S[i:(i+3)])-T))
print(min(Z))