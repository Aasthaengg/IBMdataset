a = list(map(int, input().split()))
n = [1,9,7,4]

for i in range(len(n)):
	if not(n[i] in a):
		print("NO")
		exit()

print("YES")