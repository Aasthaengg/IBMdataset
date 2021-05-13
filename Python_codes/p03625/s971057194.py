M = int(input())
A = list(map(int,input().split()))
B = {}
C = [0]*2
D = [0]*2

for i in range(len(A)):
	a = str(A[i])
	# 存在したらカウントアップ
	if (a in B): B[ str(A[i]) ] += 1 # カウント
	# 存在しなかったら 1 で初期化
	else: B[ str(A[i]) ] = 1 # カウント
	# {"1":2, "2":3, "3":1}

for i in B:
	# 一個しかなかったら条件を満たさないのでスルー
	# i: string, B[i] = count
	if B[i] < 2: continue

	# 2個以上あれば長方形にスタック
	C.append(int(i))

	# 4個以上あれば正方形にスタック
	if B[i] >= 4: D.append(int(i))

# C を降順でソート
C = sorted(C, reverse=True)

rect = C[0] * C[1]
s = max(D)
square = s * s

print(max(rect,square))