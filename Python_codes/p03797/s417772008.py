def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

N, M = cin()
if M // 2 >= N:
    ans = N
    M -= 2 * N
else:
    ans = M // 2
    M = 0
ans += M // 4
print(ans)