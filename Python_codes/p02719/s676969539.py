N, K = map(int,input().split())

rem = N % K
res = K - rem

result = [rem, res]

print(min(result))