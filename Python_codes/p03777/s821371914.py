def solve():
    a, b = input().split()

    # print(a, b)

    c = b == "H"
    return c if a == "H" else not c


if __name__ == '__main__':
    res = solve()
    print("H") if res else print("D")
