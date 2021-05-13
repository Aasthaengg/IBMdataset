N,H,W=map(int,input().split())
count=0
for i in range(N):
	A,B=map(int,input().split())
	if (A >= H) & (B >= W):
		count+=1
print(count)