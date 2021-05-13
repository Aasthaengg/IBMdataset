A=[int(input()) for _ in range(5)]
k=int(input())

if (max(A)-min(A))>k:
	print(":(")
else:
	print("Yay!")