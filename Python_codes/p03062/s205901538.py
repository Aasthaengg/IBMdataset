N = int(input())
A = list(map(int, input().split()))

minus = []
plus = []
for i in A:
    if (i < 0):
        minus.append(i)
    else:
        plus.append(i)

if (len(minus) % 2 == 0 or 0 in plus):
    # 全てを正にできる
    print(sum(plus) - sum(minus))
    exit()

# 絶対値がもっとも小さいものを探す
min_abs = 10**9 + 7
for i in A:
    min_abs = min(min_abs, abs(i))

sum_ans = 0
for i in A:
    sum_ans += abs(i)

print(sum_ans - min_abs * 2)
