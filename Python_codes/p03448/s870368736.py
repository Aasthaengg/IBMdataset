A=int(input())
B=int(input())
C=int(input())
X=int(input())

ans = 0
for i in range(A+1):
	for j in range(B+1):
		if C*50 >= X-500*i-100*j >= 0:
			ans += 1
print(ans)
