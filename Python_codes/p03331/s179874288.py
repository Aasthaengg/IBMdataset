n = int(input())

mn = 10**10
for a in range(1, n // 2+1):
    mn = min(mn, sum(int(i) for i in str(a)) + sum(int(i) for i in str(n-a)))
print(mn)
