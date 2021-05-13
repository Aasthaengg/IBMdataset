def game():
	s1 = input()
	s2 = input()
	s3 = input()
	x = s1[0]
	while len(s1)>=0 and len(s2)>=0 and len(s3)>=0:
		if x=='a':
			if len(s1)==0:
				print("A")
				return
			x = s1[0]
			s1 = s1[1:]
		if x=='b':
			if len(s2)==0:
				print("B")
				return
			x = s2[0]
			s2 = s2[1:]
		if x=='c':
			if len(s3)==0:
				print("C")
				return
			x = s3[0]
			s3 = s3[1:]
		
game()