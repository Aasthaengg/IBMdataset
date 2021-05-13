from math import factorial
 
S = int(input())
 
ans = 0
for i in range(S // 3):
    box = i + 1  # 箱の数
    ball = S - 3 * box # あらかじめ箱に３こずつ入れたあとの残りの玉の数
    ans_ = factorial(ball + box - 1) // (factorial(ball) * factorial(box - 1))
    ans += ans_
print(ans % (10 ** 9 + 7))