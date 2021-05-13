def main():
    num = list(map(int, input().split()))
    tmp = [num[1]+num[2], num[0]+num[2], num[0]+num[1]]
    if num[3] % 2 == 1:
        print(tmp[0]-tmp[1])
    else:
        print(num[0]-num[1])


if __name__ == "__main__":
    main()
