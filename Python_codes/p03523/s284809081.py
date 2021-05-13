S = input()
C = len(S)
M = S.replace("A","")
A = "AKIHABARA"
B = A.replace("A","")
P = 0

for i in range (C-1):
	if S[i] == "A":
		if S[i+1] == "A":
			P=100
	if S[i] == "K":
		if S[i+1] != "I":
			P=200
	if S[i] == "I":
		if S[i+1] != "H":
			P=200
if B==M and P<=4:
	print("YES")
else:
	print("NO")