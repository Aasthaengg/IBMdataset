S,T=open(0).read().split()
print(sum([S[i]==T[i] for i in range(3)]))