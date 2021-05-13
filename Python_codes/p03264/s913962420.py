def main():
    k = int(input())

    if k % 2:
        res = (k // 2) * (k - k // 2)
    else:
        res = (k // 2) ** 2

    print(res)

if __name__ == '__main__':
    main()