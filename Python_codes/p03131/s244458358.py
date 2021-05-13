def cin():  return list(map(int,input().split()))
K, A, B = cin()
ans1 = K + 1
kk = K - (A - 1)
ans2 = 0
if kk > 0:
    if kk % 2:  ans2 = A + 1 + kk // 2 * (B - A)
    else:  ans2 = A + kk // 2 * (B - A)
ans = max(ans1, ans2)
print(ans)