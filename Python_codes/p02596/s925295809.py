def main():
    k = int(input())

    if k % 2 ==0:
        print(-1)
        return
    last = 0
    for i in range(1000000):
        if (last*10 + 7) % k == 0:
            print(i+1)
            return
        last = (last*10 + 7) % k
    print(-1)


if __name__ == '__main__':
    main()
