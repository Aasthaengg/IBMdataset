def d(a):
	return int(a)

N=int(input())
answer=""
for i in range(N):
	if answer!="":
		answer+="\n"
	a=input().split()
	
	a.sort(key=d)
	if int(a[0])**2+int(a[1])**2==int(a[2])**2:
		answer+="YES"
	else:
		answer+="NO"
print(answer)