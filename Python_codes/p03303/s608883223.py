a = input()
b = [str(c) for c in a]
c=int(input())
d=len(b)
x=[]
for i in range(0,d,c):
	x.append(b[i])
print("".join(x))