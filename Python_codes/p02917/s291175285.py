N=int(input())
B=list(map(int,input().split()))
ans=list()
ans.append(B[0])
for i in range(1,N-1):
	if B[i]>B[i-1]:
		ans.append(B[i-1])
	else:
		ans.append(B[i])
ans.append(B[-1])
print(sum(ans))