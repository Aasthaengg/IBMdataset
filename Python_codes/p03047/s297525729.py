N, K = (int(i) for i in input().split())
if N < K:
    ans = 0
else:
    ans = N - K+1
print("{}".format(ans))
