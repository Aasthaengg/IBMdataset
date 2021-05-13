A, B = list(map(int, input().split()))
ans = B if A >= 13 else 0 if A <= 5 else B // 2
print(ans)
