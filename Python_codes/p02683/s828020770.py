n, m, x = map(int, input().split())
c = [0] * n
a = [[0] * m for i in range(n)]
for i in range(n):
    b = list(map(int, input().split()))
    c[i], a[i] = b[0], b[1::]

ans_money = 1200001

for i in range(2**n):
    b = [0]*m
    sum_money = 0
    for l in range(n):
        if i>>l & 1:
            for k in range(m):
                b[k] += a[l][k]            
            sum_money += c[l]
    if all(elem >= x for elem in b) and sum_money < ans_money:
        ans_money = sum_money
if ans_money == 1200001:
    print(-1)
else:
    print(ans_money)