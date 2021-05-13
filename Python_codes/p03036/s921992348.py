def main():
    r, D, x = (int(i) for i in input().split())

    for i in range(10):
        nx = r*x - D
        print(nx)
        x = nx


if __name__ == '__main__':
    main()
