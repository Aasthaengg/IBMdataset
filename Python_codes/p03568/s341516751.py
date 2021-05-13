def solve():
    N = int(input())
    E = [int(i) for i in input().split() if int(i) % 2 == 0]
    print(3 ** N - 2 ** len(E))

if __name__ == "__main__":
    solve()