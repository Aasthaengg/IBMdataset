def solve():
    X,Y = [int(i) for i in input().split()]
    if 2*X <= Y <= 4*X:
        if (4*X-Y) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    solve()