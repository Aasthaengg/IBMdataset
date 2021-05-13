#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
B=input_array()
A=[B[0]]
ans=B[0]

for i in range(1,n):
	if A[i-1] > B[i-1]:
		ans=ans-A[i-1]+B[i-1]
		A[i-1]=B[i-1]
	ans+=B[i-1]
	A.append(B[i-1])

print(ans)