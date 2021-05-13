n = int(input())
h = list(map(int, input().split()))

l = 0
r = 0
cnt = 0

while True:
    l = 0
    fin = False

    while h[l] == 0:
        l += 1
        if l == n:
            fin = True
            break
    if fin:
        break

    r = l
    minval = h[l]
    while h[r] != 0:
        if h[r] < minval:
            minval = h[r]

        r += 1
        if r == n:
            break

    h = h[:l] + [val - minval for val in h[l:r]] + h[r:]
    cnt += minval

print(cnt)