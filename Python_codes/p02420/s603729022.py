
while True:
	S = input()
	if S == "-":
		break
		
	N = int(input())
	for i in range(N):
		h = int(input())
		s1 = S[:h] #????????????
		s2 = S[h:] #??????
		S = s2 + s1
	
	print(S)