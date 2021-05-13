n = int(input())
a = list(map(int,input().split()))
y = [0 for _ in range(n)]
suma = sum(a)
ans = []
memo1 = 2*sum([a[j%n] for j in range(0, 0+n, 2)])-suma
memo2 = 2*sum([a[j%n] for j in range(1, 1+n, 2)])-suma
ans.append(str(memo1))
ans.append(str(memo2))
# (i+n-2)%n - (i-2)%n
for i in range(2,n):
	if i%2 == 0:
		memo1 = memo1 + 2*(a[(i+n-1)%n] - a[(i-2)%n])
		ans.append(str(memo1))
	else:
		memo2 = memo2 + 2*(a[(i+n-1)%n] - a[(i-2)%n])
		ans.append(str(memo2))
print(" ".join(ans))