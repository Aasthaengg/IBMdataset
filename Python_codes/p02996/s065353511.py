#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
AB=[input_array() for _ in range(n)]

sort_AB=sorted(AB,key=lambda x:x[1])

ans=0
flag=True
for i in sort_AB:
	ans+=i[0]
	if ans > i[1]:
		flag=False
		break

if flag:
	print("Yes")
else:
	print("No")