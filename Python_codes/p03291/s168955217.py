S=raw_input()
l=len(S)

mod=10**9+7

all_strings=1
a=0
ab=0
abc=0

for i,s in enumerate(S):
	if s =="A":
		a+=all_strings
	elif s=="B":
		ab+=a
	elif s=="C":
		abc+=ab
	elif s=="?":
		abc*=3
		abc+=ab
		ab*=3
		ab+=a
		a*=3
		a+=all_strings
	if s == "?":
		all_strings*=3

	all_strings%=mod
	a%=mod
	ab%=mod
	abc%=mod

print abc

