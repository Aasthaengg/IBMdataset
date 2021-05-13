N = int(input())
 
As = 0
Bs = 0
ABs = 0
BAs = 0
 
for i in range (0, N):
	K = str(input())
	ABs+= K.count('AB')
	if K[0] == 'B':
		if K[-1] == 'A':
			BAs+=1
		else:
			Bs+=1
	elif K[-1] == 'A':
		As+=1

if BAs== 0:
	print(ABs+min(As, Bs))
elif As+Bs>0:
	print(ABs+BAs+min(As, Bs))
else:
	print(ABs+BAs-1)