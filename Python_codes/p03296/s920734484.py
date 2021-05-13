N = int(input())
*a, = map(int, input().split())
# 何が何回連続で出現するかを記録する
Nums, Cnts = [a[0]], [1]
index = 0  # Nums,Cntsを参照するindex
for i in range(1, N):
	if a[i] == Nums[index]:
		Cnts[index] += 1
	else:
		Nums.append(a[i])
		Cnts.append(1)
		index += 1
ans = 0
for j in range(len(Cnts)):
	if Cnts[j] > 1:
		ans += Cnts[j] // 2
print(ans)
