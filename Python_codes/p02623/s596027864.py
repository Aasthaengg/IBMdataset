#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n,m,k=input2()
A=input_array()
B=input_array()
acc_A=[0]
acc_B=[0]

for i in range(n):
	acc_A.append(A[i]+acc_A[i])
for i in range(m):
	acc_B.append(B[i]+acc_B[i])

ans=0
tmp_m=m
for i in range(n+1):
	if acc_A[i]>k:
		break
	for j in range(tmp_m,-1,-1):
		if acc_B[j]<=k-acc_A[i]:
			ans=max(i+j,ans)
			tmp_m=j #探索開始地点の更新
			break
print(ans)