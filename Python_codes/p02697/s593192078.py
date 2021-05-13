n, m = map(int, input().split())

odd = (m + 1) // 2
even = m - odd

l = 1
r = 2 * odd
while l < r:
    print(l, r)
    l += 1
    r -= 1

l = n - 2 * even
r = n
while l < r:
    print(l, r)
    l += 1
    r -= 1
