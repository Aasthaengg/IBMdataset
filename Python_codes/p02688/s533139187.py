n, k = map(int, input().split())
ans = []
for i in range(k):
	d = int(input())
	for i in list(map(int,input().split())):
		ans.append(i)
print(n - len(set(ans)))