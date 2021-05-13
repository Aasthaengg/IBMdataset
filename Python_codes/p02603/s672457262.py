n = int(input())
alst = list(map(int, input().split()))
dp = [[1000, [0, 0]]]

for a in alst:
    tmp1 = max(dp[-1][0], dp[-1][1][0] * a + dp[-1][1][1])
    tmp2 = tmp1 // a
    tmp3 = tmp1 % a
    dp.append([tmp1, [tmp2, tmp3]])
print(dp[-1][0])