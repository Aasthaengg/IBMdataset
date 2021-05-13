def main():
    A, B, C = map(int, input().split())
    lst = [False] * B

    num = 0
    for _ in range(B):
        num += A
        d = num % B

        if d == C:
            flag = True
            break

        if lst[d] == True:
            flag = False
            break

        lst[d] = True

    if flag == True:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
