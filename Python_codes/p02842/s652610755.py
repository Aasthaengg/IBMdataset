# Input the amount of money Takahashi paid
N = int(input())

# Check if the price before tax is X, for X = 1, 2, 3, ..., N
ans = -1
for i in range(1, N + 1):
	if int(i * 1.08) == N:
		ans = i

# Print answer
if ans != -1:
	print(ans)
else:
	print(":(")
