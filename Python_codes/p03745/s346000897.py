def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 1
    is_add = False
    is_minus = False
    tmp = A[0]
    for a in A[1:]:
        if tmp > a:
            if is_add:
                ans += 1
                is_add = False
            else:
                is_minus = True
        elif tmp < a:
            if is_minus:
                ans += 1
                is_minus = False
            else:
                is_add = True
        tmp = a
    print(ans)


if __name__ == "__main__":
    main()
