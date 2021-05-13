s=str(input())
count=0
L=[]
for i in range(0,len(s)):
	if(s[i]=="R"):
		count+=1
	else:
		count=0
	L.append(count)
print(max(L))