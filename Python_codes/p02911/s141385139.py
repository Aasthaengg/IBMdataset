n,k,q = map(int,input().split())
a = [int(input()) for A in range(q)]
ans = [k]*(n+1)
for i in range(1,q+1):
	ans[a[i-1]] += 1
for j in range(1,n+1):
	ans[j] -= q
ans.pop(0)
for h in range(n):
	print("Yes" if ans[h] > 0 else "No")