N, X, T = list(map(int, input().split()))

shou = N // X
amari = N - X * shou

if amari == 0:
    print(T * shou)
else:
    print(T * (shou + 1))