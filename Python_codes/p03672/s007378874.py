S = input()

if len(S) % 2 != 0:
	S = S[0:len(S) - 1]
else:
	S = S[0:len(S) - 2]


while len(S) > 0:	
	if S[0:int(len(S)/2)] == S[int(len(S)/2) : len(S)]:
		print(len(S))
		break
	S = S[0:len(S) - 2]