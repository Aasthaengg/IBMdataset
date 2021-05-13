def test():
    a,b,c = map(int,input().split())
    print("YES" if 2*b == a+c else "NO")


if __name__ == "__main__":
    test()
