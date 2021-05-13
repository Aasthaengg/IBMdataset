def solve():
    N, M, L = map(int, input().split())
    
    a = L
    for i in range(10):
        a = N*a - M
        print(a)

# print(solve())

# def solve()が@return voidのとき
solve()