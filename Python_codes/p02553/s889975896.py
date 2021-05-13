x=input().split(" ")
z=[]
for i in range(2):
	z.append(int(x[i-2])*int(x[0]))
for i in range(2):
    z.append(int(x[i-2])*int(x[1]))
print(max(z))