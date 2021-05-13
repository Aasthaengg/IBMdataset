def main():
    x, y, z = map(int, input().split())
    a = list([x, y, z])
    print(a[2], a[0], a[1], sep=' ')


if __name__=="__main__":
    main()
