def main():
    x = int(input())
    cnt = x // 11 * 2
    rem = x % 11
    if rem > 6:
        cnt += 2
    elif rem > 0:
        cnt += 1

    print(cnt)

if  __name__ == '__main__':
    main()