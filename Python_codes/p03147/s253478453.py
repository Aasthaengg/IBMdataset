n = int(input())
h = list(map(int, input().split()))
count = 0
l = 0
r = 0
while True:
    for i in range(n):
        if h[i] != 0:
            l = i
            break
        if i == n - 1:
            print(count)
            exit()

    for i in range(l + 1, n):
        if h[i] == 0:
            r = i - 1
            break
        r = i

    if l == n - 1:
        r = l

    min_l_r = min(h[l:r+1])
    for i in range(l, r+1):
        h[i] -= min_l_r
    count += min_l_r
