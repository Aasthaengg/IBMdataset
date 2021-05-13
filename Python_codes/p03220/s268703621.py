n = int(input())
t, a = map(int, input().split())
heights = enumerate(map(int, input().split()))
ans = min(
    map(
        lambda x: [x[0], abs(a - (t - int(x[1]) * 0.006))]
        , heights
    )
    , key = (lambda y: y[1])
)
print(ans[0] + 1)
