N = int(input())
sum_otoshidama = 0
for _ in range(N):
    x, u = input().split()
    if u == 'JPY':
        sum_otoshidama += float(x)
    elif u == 'BTC':
        sum_otoshidama += (float(x) * 380000)
print(sum_otoshidama)
