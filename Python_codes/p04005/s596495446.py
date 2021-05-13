def solve():
    A, B, C = [int(i) for i in input().split()]
    if (A + B + C) % 2 == 0:
        print(0)
    else:
        l = sorted([A, B, C])
        print(l[0] * l[1])

if __name__ == "__main__":
    solve()
