N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(N*X)
else:
    l = K*X
    m = (N-K)*Y
    ans = l + m
    print(ans)