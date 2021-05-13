import sys
input=sys.stdin.readline
def main():
	R,C,K=map(int,input().split())
	lis=[[0]*(C) for i in range(R)]
	for i in range(K):
		a,b,c=map(int,input().split())
		lis[a-1][b-1]=c
	dp0=[[0]*(C+1) for i in range(R+1)]
	dp1=[[0]*(C+1) for i in range(R+1)]
	dp2=[[0]*(C+1) for i in range(R+1)]
	dp3=[[0]*(C+1) for i in range(R+1)]
	for i in range(1,R+1):
		for j in range(1,C+1):
			for x,y in ((dp0,0),(dp1,dp0),(dp2,dp1),(dp3,dp2)):
				t=lis[i-1][j-1]
				x[i][j]=max(x[i-1][j],x[i][j])
				x[i][j]=max(x[i][j-1],x[i][j])
				if t!=0:
					dp1[i][j]=max(dp1[i][j],x[i-1][j]+t)
					if y!=0:
						x[i][j]=max(x[i][j],y[i][j-1]+t)
	print(max(dp0[-1][-1],dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))
if __name__ == '__main__':
	main()