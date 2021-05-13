n = int(input())
a = list(map(int,input().split()))
ans = [0]*(n+1)
for i in range(len(a)):
	ans[a[i-1]] += 1
ans.pop(0)
for j in range(n):
	print(ans[j])	