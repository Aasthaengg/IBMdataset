S=input()
T=input()
PS=[S[i]==T[i] for i in range(3)]
print(sum(PS))