N, M, K = map(int, input().split())
for i in range(N+1):
	# 現在i*Mだけ黒。1列ボタンを押すと黒はi消えN-i増える
	# あと求めたい黒の数
	a = K - i*M
	if a == 0:
		print("Yes")
		exit()
	# いま作成可能な1列あたりの黒
	b = N - 2*i
	if b != 0:
		if a%b == 0 and a*b > 0 and a//b < M:
			print("Yes")
			exit()
		
print("No")