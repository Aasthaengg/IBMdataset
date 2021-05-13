def solve():
    S,W = [int(i) for i in input().split()]
    if W >= S:
        print("unsafe")
    else:
        print("safe")

if __name__ == "__main__":
    solve()