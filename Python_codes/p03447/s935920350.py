def main():
    x, a, b = [int(input()) for i in range(3)]
    ans = (x - a) % b
    print(ans)


if __name__ == '__main__':
    main()
