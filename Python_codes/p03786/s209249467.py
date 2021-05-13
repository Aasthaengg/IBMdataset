
def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    
    sm = 0
    ans = 0
    for i in range(n-1):
        sm += a[i]
        if sm * 2 >= a[i+1]:
            ans += 1
        else:
            ans = 0
    print(ans+ 1)

solve()

"""
5 6
4 7 9 3 4
"""