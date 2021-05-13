n, x, y = map(int, input().split())

ls = [0] * n
for i in range(1, n):
    for j in range(i+1, n+1):
        leng = min(abs(i - j), abs(x - i) + 1 + abs(y - j))
        ls[leng] += 1

for i in ls[1:n]:
    print(i)