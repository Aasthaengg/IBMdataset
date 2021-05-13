import sys
def input():
	return sys.stdin.readline().strip()

M, K = list(map(int, input().split()))

if K >= 2**M:
	print(-1)
	exit()


def list_print(A):
	length = len(A)
	for i in range(length - 1):
		print(A[i], end="")
		print(" ", end="")
	print(A[- 1])

if M == 1:
	if K == 0:
		list_print([0, 0, 1, 1])
		exit()
	elif K == 1:
		print(-1)
		exit()


ans = [K]

for i in range(2**M):
	if i != K:
		ans.append(i)

ans.append(K)
for i in range(2**M - 1, -1, -1):
	if i != K:
		ans.append(i)



list_print(ans)