n, m, d = map(int,input().split())

if d == 0:
    ans = n *  (m - 1) / n / n
    print("{:.10f}".format(ans))
else:
    ans = 2 * (n-d) * (m - 1) / n / n
    print("{:.10f}".format(ans))
