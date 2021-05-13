SS = list("CODEFESTIVAL2016")
S = list(input())
c = 0
for i in range(16):
	if SS[i] != S[i]:
		c += 1
print(c)