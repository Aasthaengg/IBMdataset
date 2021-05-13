n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()
ans = ab[0][0] + ab[-1][1] + (ab[-1][0] - ab[0][0])
print(ans)
