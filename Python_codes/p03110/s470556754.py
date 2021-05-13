N = int(input())

TO_JPY = {"JPY": 1, "BTC": 380000}

ans = 0

for i in range(N):
    x, u = input().split()
    x = float(x)
    ans += x * TO_JPY[u]
    
print(ans)