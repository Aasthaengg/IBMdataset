n=input()
s=raw_input()
t=raw_input()
for i in xrange(0,n+1):
	if s[i:n]==t[0:n-i]:
		print n+i
		break
