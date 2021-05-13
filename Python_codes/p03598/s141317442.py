N = int(input())
K = int(input())
x = [int(x) for x in input().split()]

res = 0
for i in range(N):
    res += 2 * min(x[i], K - x[i])
print(res)
