n, k, q = map(int, input().split())
scr = [k - q] * n
for _ in range(q):
    scr[int(input()) - 1] += 1
for i in scr:
    if i <= 0:
        print('No')
    else:
        print('Yes')