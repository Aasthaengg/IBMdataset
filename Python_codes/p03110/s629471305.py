N = int(input())

ans_jpy = 0
ans_btc = 0
for i in range(N):
    x, u = map(str, input().split())
    if u == "JPY":
        ans_jpy += int(x)
    else:
        ans_btc += float(x)
    
print(ans_jpy + ans_btc*380000)
