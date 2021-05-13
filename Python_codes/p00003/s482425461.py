n=int(input())
a_list=[]
for i in range(n):
	k=list(map(int,input().split(" ")))
	L,M,N=sorted(k)
	if L**2+M**2==N**2:
		a_list.append("YES")
	else:
		a_list.append("NO")
for i in a_list:
	print(i)