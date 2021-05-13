def main():
	N,Q=map(int,input().split())
	S=input()
	A=[0]*N
	# 累積和
	for i in range(1,N):
		A[i]=S[i-1:i+1]=="AC"
		A[i]=A[i]+A[i-1]
	# [l:r)区間の総和を求める
	for i in range(Q):
		l,r=map(int,input().split())
		print(A[r-1]-A[l-1])
if __name__=='__main__':
	main()