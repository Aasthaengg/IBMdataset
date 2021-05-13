# ABC091A - Two Coins
a, b, c = list(map(int, input().rstrip().split()))
print("Yes" if a + b >= c else "No")