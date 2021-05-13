words = {"resare" , "esare" , "remaerd" , "maerd",""}
s = input()
n = len(s)
now=""
f=0
s=s[::-1]
for i in range(0 ,n):
	now = now+s[i]
	if now in words:
		now = ""
if now in words:
	print("YES")
else:
	print("NO")