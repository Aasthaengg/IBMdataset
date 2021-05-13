def ans(S):
	Sset=set(S)
	if len(Sset)==2:
		for i in Sset:	
			if S.count(i)==2:
				print("Yes")
				return
	print("No")

S=input()
ans(S)