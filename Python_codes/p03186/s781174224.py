a, b, c = map(int, input().split())
ans = 0
if (a+b) < c:  # 解毒クッキーが足りないとき
    ans += b
    ans += (a + b) + 1  # このとき毒クッキーは最大で(a+b)+1だけ食べることができる
elif (a+b) >= c:  # 解毒クッキーが毒クッキーと個数がそれ以下のとき
    ans += c
    ans += b
print(ans)
