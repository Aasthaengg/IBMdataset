N,K = map(int, input().split() )
result = 0


if K == 1:
    result = 0
else:
    result = N-K
print(str(result))