o = str(input())
s = str(input())
n = ""

if not len(o) == len(s):
	for i in range(min(len(o),len(s))):
		n += o[i]
		n += s[i]

	if len(o) > len(s):
		n += o[len(o)-1]

else:
	for i in range(len(o)):
		n += o[i]
		n += s[i]
		
print(n)
