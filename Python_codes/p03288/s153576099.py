r=int(input())

if r<1200:
	res='ABC'
else:
	if r<2800:
		res='ARC'
	else:
		res='AGC'

print(res)