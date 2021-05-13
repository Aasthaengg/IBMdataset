N,K = (int(i) for i in input().split())

if K == 1:
    ans = 0
else:
    ans = N - K
print(ans)