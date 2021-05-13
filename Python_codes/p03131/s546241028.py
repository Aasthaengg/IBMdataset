import sys
input = sys.stdin.readline

k, a, b = [int(x) for x in input().split()]

biscuits = 0

if a + 1 > k or (b - a) <= 2:
    print(k + 1)
    sys.exit()

biscuits += b
k -= (a + 1)
biscuits += (b - a) * (k // 2) + (k % 2)

print(biscuits)