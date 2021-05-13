n, m = map(int, input().split())

num = [0] * n

for x in range(0, m):
    a, b = map(int, input().split())
    num[a-1] += 1
    num[b-1] += 1

for x in range(0, n):
    print(num[x])
