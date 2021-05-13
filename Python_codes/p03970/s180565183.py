s = "CODEFESTIVAL2016"
i = input()

c = 0

for i, j in zip(s, i):
	if i != j:
		c += 1

print(c)