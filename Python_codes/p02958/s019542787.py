n=int(input())
L=list(map(int, input().split()))
cnt=0
for i in range(n):
	if L[i]!=i+1:
		cnt+=1
if cnt>=3:
	print('NO')
else:
	print('YES')