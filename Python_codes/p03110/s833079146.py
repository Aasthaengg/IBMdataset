# input
N = int(input())

otoshidama = 0
BTC_rate = 380000.0
for i in range(1, N + 1):
    x, u = map(str, input().split())
    
    # check
    if u == "BTC":
        otoshidama += float(x) * BTC_rate
    else:
        otoshidama += float(x)

print(otoshidama)