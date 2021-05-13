def LI():
    return list(map(int, input().split()))


N, K = LI()

if K == 1:
    ans = 0
else:
    ans = N-K
print(ans)
