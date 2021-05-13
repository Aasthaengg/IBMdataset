def a(b):
	return int(b)

c=input().split()
c.sort(key=a)
ans=""
for i in range(len(c)):
	if ans!="":
		ans+=" "
	ans+=str(c[i])
print(ans)