n = int(input())
sum_i = 0  # 問題のインデックスの合計
i = 0
while sum_i < n:
    i += 1
    sum_i += i
for ans in range(1, i+1):
    if ans == sum_i - n:
        continue
    print(ans)