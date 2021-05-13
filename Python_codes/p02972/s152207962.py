n = int(input())
A = [None] + [int(i) for i in input().split()]  # 1-based index
ans = []
choose = [0] * (n + 1)


for i in range(n, 0, -1): # 大きい数から評価する
    x = sum(choose[2 * i::i]) # その箱の倍数に入っている玉の和を求める
    if x % 2 == A[i]: # 偶奇の一致を確認
        continue
    choose[i] += 1
    ans.append(str(i))

print(len(ans))
print(" ".join(ans))
