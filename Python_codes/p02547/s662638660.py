N=int(input())

cnt = 0
bOK = False
for _ in range(N):
	D1,D2 = map(int,input().split())

	if D1 == D2:
		cnt += 1
		if 3 <= cnt:
			bOK = True
	else:
		cnt = 0

if bOK:
	print("Yes")
else:
	print("No")

