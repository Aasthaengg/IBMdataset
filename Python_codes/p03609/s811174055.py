def test():
    x,t = map(int,input().split())
    print(x-t if x-t >= 0 else 0)


if __name__ == "__main__":
    test()
