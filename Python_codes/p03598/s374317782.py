N = int(input())
K = int(input())
x = list(map(int, input().split()))

a = []
res = 0

for i in range(N):
    tmp = min(2*x[i], 2*(K-x[i]))
    a.append(tmp)
    res += a[i]

print(res)