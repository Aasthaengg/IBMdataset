def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    maxL = max(L)
    sumL = sum(L) - maxL
    if maxL < sumL:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
