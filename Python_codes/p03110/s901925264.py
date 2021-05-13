def actual(n, X, U):
    # 変換: 1[BTC] == 380000.0[円]
    amount_yen = 0

    for x, u in zip(X, U):
        if u == 'JPY':
            amount_yen += x
        if u == 'BTC':
            amount_yen += x * 380000.0

    return amount_yen

n = int(input())
X = []
U = []

for _ in range(n):
  x, u = input().split()
  X.append(float(x))
  U.append(u)
  
print(actual(n, X, U))  