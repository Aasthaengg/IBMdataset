m,k=map(int,input().split())
if pow(2,m) <= k:
	print(-1)
	exit()

if m==0:
	if k==0:
		print(0,0)
	else:
		print(-1)
	exit()

if m==1:
	if k==0:
		print(0,0,1,1)
	else:
		print(-1)
	exit()
b=[]
c=[]
for i in range(pow(2,m)):
	if i!=k:
		b.append(i)
	if pow(2,m)-1-i!=k:
		c.append(pow(2,m)-1-i)

ans = " ".join([str(x) for x in b])
ans += " "
ans+=str(k)
ans += " "
ans += " ".join([str(x) for x in c])
ans += " "
ans+=str(k)

print(ans)