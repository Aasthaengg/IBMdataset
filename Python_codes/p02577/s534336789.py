N = int(input())

N_letter = str(N)
M = (len(N_letter))
S = 0
for i in range(M):
	S = S + int(N_letter[i])

if (S/9) ==  int(S/9):
	print("Yes")
else:
	print("No")