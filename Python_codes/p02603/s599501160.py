N = int(input())  # N日間
A = list(map(int, input().split()))  # i日目の株の値段
money = 1000
stocks = 0
for i in range(N-1):
    # print("本日の値段 : ", A[i])
    # print("現在の現金 : ", money)
    # print("現在の株数 : ", stocks)
    # 次の日に上がるなら有り金全部株と交換する
    if A[i+1] > A[i] and money >= A[i]:
        # i日目に株を買う
        stocks = money // A[i]
        money -= (money // A[i])*A[i]
    # 次の日に下がる&今株を持っているのであれば，全部お金にする
    if A[i+1] < A[i] and stocks > 0:
        money += stocks*A[i]
        stocks = 0
print(money + stocks*A[-1])
