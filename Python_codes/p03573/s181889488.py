def main():
    *args, = map(int, input().split())
    args.sort()
    if args[0] == args[1]:
        print(args[2])
        return

    print(args[0])


if __name__ == '__main__':
    main()
