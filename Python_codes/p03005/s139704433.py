import sys

n, k = [int(i) for i in input().split()]

if k == 1:
    print(0)
    sys.exit()

ans = n - k
print(ans)
