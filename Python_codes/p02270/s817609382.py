n, k = map(int, input().split())
W = [int(input()) for i in range(n)]

left = max(W)
ans = right = 100000 * 100000


def is_ok(P):
    truck = 1
    t_sum = 0
    for i in range(n):
        if t_sum + W[i] <= P:
            t_sum += W[i]
        else:
            truck += 1
            t_sum = W[i]
            if truck > k:
                return False
    return True


while left <= right:
    mid = (left + right) // 2
    if is_ok(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)

