n = int(input())
p = [int(input()) for _ in range(n)]

# 数列を並び替えたとき、元のインデクス位置が単調増加となる区間は取り出し不要
# n - 最長区間を引いたものが最短手数となる
p_with_index = list(sorted(enumerate(p), key=lambda x : x[1]))
max_inc_span = 1
span = 1
for i in range(1, n):
    if p_with_index[i-1] < p_with_index[i]:
        span += 1
        max_inc_span = max(max_inc_span, span)
    else:
        span = 1

print(n - max_inc_span)