def main():
    f, t = [int(v) for v in input().split(' ')]
    count = 0
    d = 1
    tmp = f
    while True:
        tmp = tmp * 2
        if tmp > t:
            break
        count += 1

    print(count + 1)



if __name__ == '__main__':
    main()
