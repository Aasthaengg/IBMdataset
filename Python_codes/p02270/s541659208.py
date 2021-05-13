def f(n, k, W):
    sum = 0
    i = 0
    while k > 0 and i < len(W):
        sum += W[i]
        if sum <= n:
            i += 1
        else:
            sum = 0
            k -= 1
    if k == 0:
        return False
    else:
        return True


n ,k = [int(_) for _ in input().split()]
W = []
for i in range(n):
    W.append(int(input()))
low = 0
high = 10 ** 9
while low + 1 < high:
    mid = (low + high) // 2
    # print("mid", mid)
    # print("low", low)
    # print("high", high)
    # print("f", f(mid, k, W))
    # print("-----------------------")
    if f(mid, k, W):
        high = mid
    else:
        low = mid
print(high)

