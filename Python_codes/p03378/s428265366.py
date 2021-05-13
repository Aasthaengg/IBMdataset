N,M,X=map(int,input().split())
A=list((map(int,input().split())))

ans = 0
for i in A:
	ans += X>i
	
ans_N = 0
for i in A:
	ans_N += X<i

print(min(ans,ans_N))
