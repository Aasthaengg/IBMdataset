def maxStack(k, p, W):
    nw = 0
    count = 0
    t = 1
    for x in W:
        if x > p:
            return count
        if nw + x <= p:
            nw += x
            count += 1
        else:
            if t == k:
                return count
            else:
                t += 1
                nw = x
                count += 1
    return count


n, k = map(int, raw_input().split())
W = [int(raw_input()) for i in xrange(n)]

left = 1
right = sum(W)
while left < right:
    mid = (left + right) / 2
    v = maxStack(k, mid, W)
    if v >= n:
        right = mid
    else:
        left = mid + 1
print left