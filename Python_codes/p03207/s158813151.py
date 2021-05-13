n= int(input())
L=[]
for i in range(n):
	a=int(input())
	L.append(a)

print(sum(L)-max(L)//2)