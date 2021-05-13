A, B, Q = [int(x) for x in input().split()]
s = [-10 ** 10] + [None] * A + [2 * (10 ** 10)]  # s[0], s[A+1]はダミー
t = [-10 ** 10] + [None] * B + [2 * (10 ** 10)]  # t[0], t[B+1]はダミー
x = [0] * Q
for i in range(1, A + 1):
    s[i] = int(input())
for j in range(1, B + 1):
    t[j] = int(input())
for k in range(Q):
    x[k] = int(input())

for i in range(Q):
    # Find s[j] such that s[j] <= x[i] < s[j+1]
    ok = 0       # s[0] < x[i]
    ng = A + 1   # x[i] < s[A+1]
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if s[mid] < x[i]:
            ok = mid
        else:
            ng = mid
    j = ok

    ok = 0      # t[0] < x[i]
    ng = B + 1  # x[i] < t[A+1]
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if t[mid] < x[i]:
            ok = mid
        else:
            ng = mid
    k = ok
 
    ans = min(  max(s[j + 1], t[k + 1]) - x[i], # 右
                x[i] - min(s[j], t[k]),         # 左
                2 * s[j + 1] - t[k] - x[i],     # 右 s[j+1] -> 左 t[k]
                s[j + 1] - 2 * t[k] + x[i],     # 左 t[k] -> 右 s[j+1]
                -s[j] + 2 * t[k + 1] - x[i],    # 右 t[k+1] -> 左 s[j]
                -2 * s[j] + t[k + 1] + x[i])    # 左 s[j] -> 右 t[k+1]

    print(ans)
