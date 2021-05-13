M, K = [int(_) for _ in input().split()]
if [M, K] == [1, 0]:
    print(0, 0, 1, 1)
elif K >= 2**M or K == M == 1:
    print(-1)
else:
    ans = list(range(2**M))
    ans.pop(K)
    print(*([K] + ans + [K] + ans[::-1]))
# https://img.atcoder.jp/abc126/editorial.pdf
