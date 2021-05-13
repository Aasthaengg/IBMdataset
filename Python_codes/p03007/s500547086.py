# 最後の計算で(max)-(min)が必要
# max: 最大値 - ∑負の数
# min: 最小値 - ∑正の数

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = []
low = A[0]
high = A[-1]

for a in A[1:-1]:
    if a > 0:
        ans.append((low, a))
        low = low - a
    else:
        ans.append((high, a))
        high = high - a

ans.append((high, low))

print(high - low)
for (x, y) in ans:
    print(x, y)