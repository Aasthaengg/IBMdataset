O = input()
#atcoderbeginnercontest

E = input()
#atcoderregularcontest
S = []

if len(O) == len(E):
	for i in range(len(O)):
		S.append(O[i] + E[i])
else:
	for i in range(len(E)):
		S.append(O[i] + E[i])
	S.append(O[-1])
#print(S)
print("".join(S))