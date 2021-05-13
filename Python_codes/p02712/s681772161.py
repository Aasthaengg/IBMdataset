# 入力
n = int(input())

# 出力
answer = 0
for i in range(1, n + 1):
    if not i % 3 == 0 and not i % 5 == 0:
        answer += i

print(answer)
