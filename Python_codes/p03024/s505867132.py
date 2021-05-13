s = input()

l = len(s)
temp = 0
for i in s:
	if i =="o":
		temp+=1

if (8-temp) <= 15-l:
	print("YES")
else:
	print("NO")