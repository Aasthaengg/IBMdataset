str = input()

N = int(str.split()[0])
K = int(str.split()[1])
if (K == 1):
	s = 0
else :
	s = N - K

print("{}".format(s))
