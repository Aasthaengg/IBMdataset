def test():
    a,b = map(int,input().split())
    c = a * b
    d = a - b
    f = a + b
    s = list([c,d,f])
    print(max(s))


if __name__ == "__main__":
    test()
