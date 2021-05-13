
alphabet = [0]*26
i = 0;
for j in range(97,123):
	alphabet[i] = chr(j)
	i += 1
al_count = [0]*26
while True :
	try :
		words = raw_input().lower().split()
		for k in words :
			for l in list(k):
				if l=='a':
					al_count[0] += 1
				elif l=='b':
					al_count[1] += 1
				elif l=='c':
					al_count[2]+=1	
				elif l=='d':
					al_count[3] += 1
				elif l=='e':
					al_count[4]+=1
				elif l=='f':
					al_count[5] += 1
				elif l=='g':
					al_count[6]+=1
				elif l=='h':
					al_count[7] += 1
				elif l=='i':
					al_count[8]+=1
				elif l=='j':
					al_count[9] += 1
				elif l=='k':
					al_count[10]+=1	
				elif l=='l':
					al_count[11] += 1
				elif l=='m':
					al_count[12]+=1	
				elif l=='n':
					al_count[13] += 1
				elif l=='o':
					al_count[14]+=1
				elif l=='p':
					al_count[15] += 1
				elif l=='q':
					al_count[16]+=1
				elif l=='r':
					al_count[17] += 1
				elif l=='s':
					al_count[18]+=1
				elif l=='t':
					al_count[19] += 1
				elif l=='u':
					al_count[20]+=1
				elif l=='v':
					al_count[21]+=1
				elif l=='w':
					al_count[22] += 1
				elif l=='x':
					al_count[23]+=1
				elif l=='y':
					al_count[24] += 1
				elif l=='z':
					al_count[25]+=1
	except :
		break
for i in range(26):
	print '%c : %d' %(alphabet[i],al_count[i])