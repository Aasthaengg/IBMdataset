# A - Simple Calculator
x,y = map(int,input().split())

# 初めと終わりに B を押すとき
ans1 = -y - (-x) + 2
# 初めだけ B を押すとき
ans2 = y - (-x) + 1
# 終わりだけ B を押すとき
ans3 = -y - x + 1
# B を押さないとき
ans4 = y - x

ans = [ans1,ans2,ans3,ans4]
ans = [a for a in ans if a > 0]
ans = min(ans)
print(ans)