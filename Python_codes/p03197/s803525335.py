def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    flag = False
    for a in A:
        if a % 2:
            flag = True
    if flag:
        print("first")
    else:
        print("second")


if __name__ == '__main__':
    main()
