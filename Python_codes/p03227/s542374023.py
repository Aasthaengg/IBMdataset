s=input()
if(len(s)==2):
	print(s)
else:
	r=""
	for i in range(len(s)):
		r+=s[-i-1]
	print(r)