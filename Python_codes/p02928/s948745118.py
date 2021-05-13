n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [sorted(a).index(a[i]) for i in range(n)]
p = [b[i] * (k*(k+1)//2)for i in range(n)]
q = [0] * n
for i in range(n):
    num = 0
    for j in range(i,n):
        if a[j] > a[i]:
            num += 1
    q[i] = num
ans = sum(p)-sum(q)*k
print(ans%1000000007)