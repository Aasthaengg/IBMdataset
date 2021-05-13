n = int(input())
arr = []
for i in range(0 , n):
	arr.append(int(input()))
gp =[]
p=0
for i in range(0 ,n):
	arr[i]=arr[i]-1
cnt =0
vis =[0 for i in range(0 , n+1)]
while True:
	if p==1:
		print (cnt)
		break
	if cnt>=n:
		print(-1)
		break
	cnt = cnt+1
	p = arr[p]

