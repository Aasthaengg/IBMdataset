
def solve():

    N = int(input())
    xlist = []

    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "BTC":
            xlist.append(x*380000.0)
        else:
            xlist.append(x)

    print(sum(xlist))


if __name__ == "__main__":
    solve()
