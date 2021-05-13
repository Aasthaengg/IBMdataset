a, b, c, = map(int , input().split())
for i in range(0 , 100100):
	if (b*i+c)%a==0:
		print("YES")
		exit()

print("NO")