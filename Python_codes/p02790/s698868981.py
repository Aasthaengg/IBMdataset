def main():

    a, b = map(int, input().split())
    s = str(a) * b
    t = str(b) * a
    if s < t:
        return s
    return t


if __name__ == '__main__':
    print(main())
