S = input()

count = 0
for i, s in enumerate(S):
	count += (s != "CODEFESTIVAL2016"[i])
print(count)
