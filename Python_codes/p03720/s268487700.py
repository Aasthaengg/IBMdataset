n, m = map(int, input().split())
count = [0] * n
for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n):
        if j + 1 in a:
            count[j] += 1
for i in range(n):
    print(count[i])