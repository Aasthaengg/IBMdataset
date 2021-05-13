N=int(input())

A=[[0]*2 for i in range(N)]

for i,x in enumerate(input()):
	A[i][0]=ord(x)
for i,x in enumerate(input()):
	A[i][1]=ord(x)

t=[]
f=True
for x,y in A:
	if f:
		if x==y:
			t.append(0)
		else:
			t.append(1)
			f=False
	else:
		f=True

ans=1
if t[0]==0:ans*=3
else:ans*=6


for i in range(1,len(t)):
	if t[i-1]==t[i]==0:
		ans=(ans*2)%(1000000007)
	elif t[i-1]==0 and t[i]==1:
		ans=(ans*2)%(1000000007)
	elif t[i-1]==1 and t[i]==1:
		ans=(ans*3)%(1000000007)

print(ans)