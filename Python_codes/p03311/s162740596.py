# from statistics import median

n = int(input())
a = map(int, input().split())
a = tuple(sorted(x - i for i, x in enumerate(a, 1)))

# b = median(a)
b = a[n // 2]  # 要素が偶数個のとき、中央値の計算に使用する2値のいずれでもよい

ans = sum(abs(x - b) for x in a)
print(ans)
