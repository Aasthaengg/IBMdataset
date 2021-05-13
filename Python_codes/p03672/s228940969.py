import math
S = str(input())
S=S[0:len(S)-1]
 
if len(S)%2!=0:
	S=S[0:len(S)-1]
 
for i in range (0, int(len(S)/2)):
	N = len(S)
	if S[0:int(N/2)] == S[int(N/2)::]:
		print(2*len(S[0:int(N/2)]))
		exit()	
	else:
		S=S[0:N-2]