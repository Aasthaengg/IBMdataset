
def main():
    X = int(input())
    maxX = 0
    time = 0
    while maxX < X :
        time += 1
        maxX += time

    print(time)


if __name__ == '__main__':
    main()
