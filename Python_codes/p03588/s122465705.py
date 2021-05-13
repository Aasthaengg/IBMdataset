N=int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]
ab.sort(key=lambda x: x[0])
ans = ab[-1][0] + ab[-1][1]
print(ans)