a, b, c, k = map(int,input().split())
print("Unfair" if abs(a-b) >= 1e18 else a-b if k % 2 == 0 else b-a)