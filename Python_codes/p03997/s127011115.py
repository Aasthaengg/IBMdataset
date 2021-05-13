def main():
    length = [int(input()) for _ in range(3)]
    print(sum(length[:2]) * length[2] // 2)


if __name__ == '__main__':
    main()

