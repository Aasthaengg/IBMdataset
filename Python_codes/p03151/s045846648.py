def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    sA = sum(A)
    sB = sum(B)
    if sA < sB:
        return print(-1)
    C = [a-b for a, b in zip(A, B)]
    C.sort()
    ans = 0
    less = 0
    for c in C:
        if c < 0:
            ans += 1
            less += c
        else:
            break
    for c in C[::-1]:
        if 0 <= less:
            break
        less += c
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
