n, m = map(int, raw_input().split(" "))
a = [[0 for j in range(m)] for i in range(n)]
b = [0 for j in range(m)]
for i in range(n):
    a[i] = map(int, raw_input().split(" "))
for j in range(m):
    b[j] = input()

for i in range(n):
    ans = 0
    for j in range(m):
        ans += a[i][j] * b[j]
    print(ans)