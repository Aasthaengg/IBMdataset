N = int(input())
D,X =map(int,input().split())
A = [int(input()) for a in range(N)]
cnt = 0
for i in range(N):
	for l in range(100):
		if A[i]*l+1 <= D:
			cnt += 1
		else:
			break
print(cnt+X)
