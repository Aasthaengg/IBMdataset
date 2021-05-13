def solve():
    N, A, B = map(int, input().split())

    if ((B-1)-A)%2 == 1:
        print("Alice")
    else:
        print("Borys")

if __name__ == "__main__":
        solve()
