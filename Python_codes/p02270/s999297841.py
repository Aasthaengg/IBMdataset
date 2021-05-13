def luggage_num(P):
    i = 0
    for _ in range(k):
        t = 0
        while t + w[i] <= P:
            t += w[i]
            i += 1
            if i == n:
                return n
    return i

n, k = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))

right = n * max(w)
left = 0

while right - left > 1:
    mid = int((right + left) / 2)
    if luggage_num(mid) >= n:
        right = mid
    else:
        left = mid
print(right)
