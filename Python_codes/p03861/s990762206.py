if __name__ == '__main__':
    a, b, x = map(int, input().split())
    l = b // x
    r = (a-1) // x
    print(l - r)