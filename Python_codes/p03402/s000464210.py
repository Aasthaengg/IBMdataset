k=50
a,b=map(int,input().split())
a-=1;b-=1
ans=[["#"for _ in range(2*k)]for _ in range(2*k)]
for i in range(k):
	for j in range(2*k):
		ans[i][j]="."
for i in range(k-1):
	if b>0:
		for j in range(i%2*2,2*k,4):
			if b>0:
				ans[i][j]="#"
				b-=1
			else:
				break
for i in range(k+1,2*k):
	if a>0:
		for j in range(i%2*2,2*k,4):
			if a>0:
				ans[i][j]="."
				a-=1
			else:
				break
print(2*k,2*k)
for i in range(2*k):
	print("".join(ans[i]))