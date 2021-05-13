A, B, C, K = map(int, input().split())

gap = A - B if K % 2 == 0 else B - A

ans = gap if gap <= 10**18 else 'Unfair'
print(ans)
