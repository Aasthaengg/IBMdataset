N = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
res, point = 0, 0
for i in range(N):
    point = sum(a1[:i+1]) + sum(a2[i:N])
    res = max(res, point)
print(res)