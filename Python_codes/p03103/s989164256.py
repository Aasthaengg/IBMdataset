n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
money = 0
num = 0
for i in range(n):
    if num + ab[i][1] > m:
        break
    money += ab[i][0] * ab[i][1]
    num += ab[i][1]
print(money + (m-num) * ab[i][0])