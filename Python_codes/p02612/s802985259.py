def solve():
    N = int(input())
    change = N % 1000
    if change == 0:
        print(0)
    else:
        print(1000 - change)

if __name__ == "__main__":
    solve()