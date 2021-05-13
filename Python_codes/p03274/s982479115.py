
def solve():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ans = float('inf')
    for i in range(n):
        if i + 1 >= k:
            l = a[i - k + 1]
            r = a[i]
            ans = min(ans, r - l + min(abs(l), abs(r)))
    print(ans)

solve()

"""
5 6
4 7 9 3 4
"""