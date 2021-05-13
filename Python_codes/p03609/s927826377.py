X, t = map(int, input().split())
# AにX - t 代入し、　－の値を0に変換
A = X - t
A = max(0, A)
print(A)