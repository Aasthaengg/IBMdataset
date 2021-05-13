def main():
    D, T, S = map(int, input().split())
    if T * S >= D:
        print('Yes')
        return
    else:
        print('No')
        return


if __name__ == '__main__':
    main()
