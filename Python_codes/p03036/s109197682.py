r,D,x = map(int,input().split())
ans = r*x - D
print(ans)
for i in range(9):
	ans = r*ans - D
	print(ans)