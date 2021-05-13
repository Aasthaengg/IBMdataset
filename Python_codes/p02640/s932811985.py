def test():
    x, y = map(int, input().split())
    if y&1:
        print("No")
        return
    print("Yes" if 2*x<=y<= 4*x else "No")
test()