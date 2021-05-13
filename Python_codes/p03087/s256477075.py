N,Q=map(int,input().split())
S=input()
A=[0]*N
# 累積和
for i in range(1,N):
	if S[i-1:i+1]=="AC":
		A[i]+=1
	A[i]=A[i]+A[i-1]
# [l:r)区間の総和を求める
for i in range(Q):
	l,r=map(int,input().split())
	print(A[r-1]-A[l-1])