N, K = list(map(int, input().split()))

if K == 1:
    ans = 0
else:
    min_ = 1
    max_ = N - (K - 1)  # K-1人に一つずつ配った残り
    ans = max_ - min_

print(ans)