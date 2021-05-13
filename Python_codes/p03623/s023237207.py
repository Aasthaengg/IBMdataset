def solve():
    x, a, b = map(int, input().split())
    if min(abs(a-x), abs(b-x)) == abs(a-x):
        print("A")
    else:
        print("B")
    return 0

if __name__ == "__main__":
    solve()
