N, L = map(int, input().split())
a = [L + i for i in range(N)]
ans = 1000
index = 0
for i in range(N):
    if ans > abs(a[i]):
        ans = abs(a[i])
        index = i

print(sum(a) - a[index])