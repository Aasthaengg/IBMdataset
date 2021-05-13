n, m = map(int, input().split())
List1 = [[0 for i in range(m)] for i in range(n)]
for x in range(n):
    List1[x] = list(map(int, input().split()))
List2 = [int(input()) for i in range(m)]
sum = [0 for i in range(n)]
for x in range(n):
    for y in range(m):
        sum[x] += List1[x][y] * List2[y]
for x in range(n):
    print(sum[x])
