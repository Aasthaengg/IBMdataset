x = input()
s = ""
if x[0] == "?":
	s = s+ "D"
else:
	s = s + x[0]
for i in range(1,len(x)):
	if x[i] == "?":
		s = s + "D"
		continue
	s = s + x[i]
print(s)