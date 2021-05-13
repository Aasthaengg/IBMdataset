N = int(input())
a = [0] + list(map(int, input().split()))
box = [0] * (N + 1)
ans = []

# ex. 3の倍数は 3*1, 3*2, ..., 3*(N//3 - 1), 3*(N//3)

# 箱Nから確定させていく (箱番号が大きいものほど、考慮すべき箱の数が少ない)

# 箱iについて
for i in range(N, 0, -1):
    cnt = 0
    # 2*i, 3*i, ..., N//i * i について、現在のボールの総和
    for j in range(N // i, 1, -1):
        cnt += box[i * j]
    # 既に偶奇が満たされている場合
    if cnt % 2 == a[i]:
        box[i] = 0
    # 偶奇が満たされていない場合
    else:
        box[i] = 1
        ans.append(i)

ans = ans[::-1]
print(len(ans))
if len(ans) > 0:
    print(*ans)
