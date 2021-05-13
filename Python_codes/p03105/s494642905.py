
def solve():

    A, B, C = map(int, input().split())

    canListen = B//A

    print(min(canListen, C))


if __name__ == "__main__":
    solve()
