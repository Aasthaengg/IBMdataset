shape = list(map(int, input().split()))
shape.sort()
N, M = shape
# print(N, M)

if N == 1:
    if M > 2:
        ans = M - 2
    else:
        ans = M
elif N == 2:
    ans = 0
else:
    ans = (N - 2) * (M - 2)
print(ans)
