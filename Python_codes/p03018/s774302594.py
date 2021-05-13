s=input().replace("BC","X").replace("B","Y").replace("C","Y")
a=False
ans=0
c=0
for i in "Y"+s+"Y":
	if i=="A":
		a=True
		c+=1
	if i=="X":
		if a:
			ans+=c
	if i=="Y":
		a=False
		c=0
print(ans)