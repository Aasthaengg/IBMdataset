import sys
n, m, k = [int(i) for i in sys.stdin.readline().split()]
flg = False
for y in range(n + 1):
    for x in range(m + 1):
        if y * (m - x) + x * (n - y) == k:
            flg = True
if flg:
    print("Yes")
else:
    print("No")