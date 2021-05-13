n, k = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
x = 0
i = 0
while x < k:
    x += ab[i][1]
    i += 1
print(ab[i-1][0])