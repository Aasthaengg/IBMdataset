a,b,c=map(int,input().split())
li=[a,b,c]
li=sorted(li)

if li[2]==li[0]==li[1]:
	ans="Yes"
else:
	ans="No"
print(ans)

