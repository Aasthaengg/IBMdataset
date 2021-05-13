def solve_127b(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

r, d, x = map(int, input().split())
solve_127b(r, d, x)