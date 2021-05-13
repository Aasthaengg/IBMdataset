N, K = [int(x) for x in input().split()]

if N % 2 == 0:
	if K <= int(N/2):
		print("YES")
	else:
		print("NO")
else:
	if K <= int(N/2)+1:
		print("YES")
	else:
		print("NO")