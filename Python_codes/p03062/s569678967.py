n = int(input())
a = list(map(int,input().split()))
"""
マイナスの数偶数→いける
マイナスの数奇数→１こあまる
"""
b = [abs(a[i]) for i in range(n)]


"""
マイナスの個数は
"""
tmp = 0
for i in a:
	if i < 0:
		tmp += 1

if tmp % 2 == 0:
	print(sum(b))
else:
	sumb = sum(b)
	ans = 0
	for i in range(n):
		ans = max(sumb-2*b[i], ans)
	print(ans)