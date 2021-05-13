a, b, c = map(int, input().split())
# 少なくとも一つ、奇数が存在する場合
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0)
    exit()
# 全て偶数で、A=B=Cの場合
if a == b and b == c:
    print(-1)
    exit()

cnt = 0

while True:
    cnt += 1
    next_a = b // 2 + c // 2
    next_b = a // 2 + c // 2
    next_c = a // 2 + b // 2
    a = next_a
    b = next_b
    c = next_c
    # 処理を行った結果、奇数が発生してしまったらそこで終了
    # 奇数がなければwhileを続ける
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        break

print(cnt)