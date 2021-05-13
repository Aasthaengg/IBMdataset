N, K = map(int, input().split())
a = N//K
b = N-K
if K == 1:
    print(0)
else:
    print(b-a+1)
