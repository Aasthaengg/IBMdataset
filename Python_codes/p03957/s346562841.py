s=raw_input()
l=len(s)

for i in range(l):
	for j in range(i,l):
		if s[i]+s[j]=="CF":
			print "Yes"
			quit()
else:
	print "No"