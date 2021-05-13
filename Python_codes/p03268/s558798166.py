N, K = map(int, input().split())
if K % 2 != 0:
    tmp = (N//K)
    if tmp == 0:
        ans = 0
    else:
        ans = tmp ** 3
else:
    K = K//2
    tmp = (N//K)
    if tmp == 0:
        ans = 0
    else:
        tmp1 = tmp//2
        tmp2 = tmp - tmp1
        ans = tmp2**3 + tmp1**3

print(ans)