X = input()

if X[0] == 1:
	X2 = [9]*(len(X) - 1)
elif X[1:].count("9") == len(X[1:]):
	X2 = X
else:
	tmp = int(X[0])-1
	X2 = [str(tmp)] + ["9"]*(len(X)-1)


print(sum(list(map(int, X2))))