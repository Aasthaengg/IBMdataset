N,M = list(map(int,input().split()))
AB = [list(map(int,input().split())) for i in range(N)]
AB_sorted = sorted(AB, key=lambda x: x[0])

money = 0
drink = 0
for i in range(N):
    drink += AB_sorted[i][1]
    money += AB_sorted[i][0] * AB_sorted[i][1]
    if drink >= M:
        money -= (drink - M) * AB_sorted[i][0]
        break
print(money)