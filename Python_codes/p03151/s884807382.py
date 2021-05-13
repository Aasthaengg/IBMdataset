n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff_AB = sum(A) - sum(B)

if diff_AB < 0:
	print(-1)
	exit()

Diff = []	
for i in range(n):
	diff = A[i] - B[i]
	Diff.append(diff)

Diff = sorted(Diff)

res = 0
for i in range(n):
	if Diff[i] < 0:
		res += 1
	else:
			if Diff[i] <= diff_AB:
				diff_AB -= Diff[i]
			else:
				diff_AB = 0
				res += 1

if diff_AB > 0:
	res += 1

print(res)
