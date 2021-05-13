S = input()
count = 0
mcount = 0
for i in range(len(S)):
	if(S[i] == 'S'):
		count = 0
	elif(S[i] == 'R'):
		count += 1
		if(count>mcount):
			mcount = count
print(mcount)


