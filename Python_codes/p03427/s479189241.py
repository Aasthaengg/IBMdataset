def solve():
    N = input()
    if len(N) == 1:
        print(int(N))
    elif all(i == '9' for i in N[1:]):
        print(int(N[0]) + 9 * (len(N) - 1))
    else:
        print((int(N[0]) - 1) + 9 * (len(N) - 1))

if __name__ == "__main__":
    solve()