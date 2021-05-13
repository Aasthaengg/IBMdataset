n, m = map(int, input().split())
a = list(map(int, input().split()))

x = [-float('inf')] * (n + 1)
x[0] = 0
l = [0] * (n + 1)
_c = [2,5,5,4,5,6,3,7,6]
c = dict()
for i in range(m):
    c[a[i]] = _c[a[i] - 1]

for i in range(1, n + 1):
    x_max = -float('inf')
    l_max = 0
    for digit in c.keys():
        left = i - c[digit]
        if left >= 0:
            tmp_x = digit * (10 ** l[left]) + x[left]
            tmp_l = l[left] + 1
            if tmp_x > x_max:
                x_max = tmp_x
                l_max = tmp_l

    x[i] = x_max
    l[i] = l_max
print(x[-1])
