N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
cnt = 0
e,m,h = 0,0,0
for i in range(N):
	if P[i] <= A:
		e+=1
	elif P[i] <= B:
		m+=1
	else:
		h+=1
ans = min(min(e,m),h)
print(ans)