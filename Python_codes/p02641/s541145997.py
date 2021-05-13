X, N = map(int, input().split())
P = list(map(int, input().split()))

Q = [q for q in range(-1, 102) if q not in P]  # -1以上101以下整数のうちPに存在しないもの
ans = min(Q, key=lambda q: (abs(q - X), q))  # maspyさん解法
print(ans)