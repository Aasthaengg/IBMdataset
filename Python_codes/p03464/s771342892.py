def getlist():
	return list(map(int, input().split()))

#受け取り
K = int(input())
A = getlist()
A = A[::-1]

#処理
ans = 0
dpM = [0] * (K)
dpm = [0] * (K)
dpM[0] = A[0] * 2 - 1
dpm[0] = A[0]
for i in range(1, K):
	if A[i] > dpM[i - 1]:
		ans = -1
		break
	elif A[i] >= dpm[i - 1]:
		dpM[i] = A[i] * 2 - 1
		dpm[i] = A[i]

	else:
		dpM[i] = A[i] * (dpM[i - 1] // A[i] + 1) - 1

		if dpm[i - 1] % A[i] == 0:
			dpm[i] = dpm[i - 1]
		else:
			dpm[i] = A[i] * (dpm[i - 1] // A[i] + 1)
	if dpm[i] > dpM[i]:
		ans = -1
		break

#出力
if ans == -1 or A[0] != 2:
	print(-1)
else:
	print(dpm[-1], dpM[-1])