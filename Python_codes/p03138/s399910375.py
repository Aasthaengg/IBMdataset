n, k = map(int, input().split())
a = list(map(int, input().split()))

length = len(bin(max(max(a), k))[2:])
n_1 = [0] * length

for i in range(n):
    abin = bin(a[i])[2:].zfill(length)
    for j in range(length):
        if abin[j] == '1':
            n_1[j] += 1

def search(i, left_w):
    if i >= length:
        return 0

    w1 = 2 ** (length - i - 1)
    w0 = 0
    v1 = (n - n_1[i]) * 2 ** (length - i - 1)
    v0 = n_1[i] * 2 ** (length - i - 1)

    if left_w >= 2 * w1:
        if v1 > v0:
            return v1 + search(i+1, left_w - w1)
        else:
            return v0 + search(i+1, left_w - w0)

    if left_w >= w1 and v1 >= v0:
        return max(v1 + search(i+1, left_w - w1), v0 + search(i+1, left_w - w0))
    else:
        return v0 + search(i+1, left_w - w0)

print(search(0, k))
