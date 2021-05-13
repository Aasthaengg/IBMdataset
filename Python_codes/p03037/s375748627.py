N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
	l, r = map(int, input().split())
	L.append(l)
	R.append(r)

L_max = 0
R_min = 100000

for i in range(M):
	L_max = max(L_max, L[i])
	R_min = min(R_min, R[i])

cnt = R_min - L_max + 1

if cnt < 0:
	print("0")
else:
	print(cnt)
