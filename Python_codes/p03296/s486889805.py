def ContinueCnt(A):
	Datas, Cnts = [A[0]], [1]
	index = 0
	for i in range(1, len(A)):
		if A[i] == Datas[index]:
			Cnts[index] += 1
		else:
			Datas.append(A[i])
			Cnts.append(1)
			index += 1
	return Datas, Cnts

N = int(input())
*a, = map(int, input().split())
Nums, Cnts = ContinueCnt(a)
ans = 0
for j in range(len(Cnts)):
	if Cnts[j] > 1:
		ans += Cnts[j] // 2
print(ans)
