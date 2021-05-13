n=int(input())
h=list(map(int,input().split()))

check=0
for i in h:
	if check-1>i:
		print("No")
		exit()
	check=max(check,i)
print("Yes")