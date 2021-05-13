def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    num2 = 0
    num4 = 0

    for i in range(n):
        a = inlis[i]
        if a % 4 == 0:
            num4 += 1
        elif a % 2 == 0:
            num2 += 1
    if n <= 3:
        if num4 >=1:
            print('Yes')
        elif num2 == n:
            print('Yes')
        else:
            print('No')
    else:
        if num2 + (2*num4) >= n:
            print("Yes")
        else:
            if n % 2 != 0 and num2 + (2*num4 +1) >= n:
                print('Yes')
            else:
                print('No')





if __name__ == "__main__":
    main()