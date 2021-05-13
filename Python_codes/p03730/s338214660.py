A,B,C=map(int,input().split())
x=A%B
y=max(A,B)
for i in range(y+1):
	if (x*i)%B==C:
		print("YES")
		exit()
print("NO")