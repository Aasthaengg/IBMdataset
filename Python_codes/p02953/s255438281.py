def main():
    N = int(input())
    H = [int(i) for i in input().split()]

    flag = True
    for i in range(N-1)[::-1]:
        if H[i] > H[i+1]:
            if H[i] - H[i+1] == 1:
                H[i] -= 1
            else:
                flag = False

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
