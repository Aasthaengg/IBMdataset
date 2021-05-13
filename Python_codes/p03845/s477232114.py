n = int(input())
t = list(map(int, input().split()))
sum = sum(t)
m = int(input())
px = [list(map(int, input().split())) for i in range(m)]
for j in range(m):
    p, x = px[j]
    print(sum - t[p-1] + x)
