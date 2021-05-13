def solve(n, x, t):
    times = -(-n // x)
    return t * times

if __name__ == "__main__":
    n, x, t = map(int, input().split(' '))
    print(solve(n, x, t))
