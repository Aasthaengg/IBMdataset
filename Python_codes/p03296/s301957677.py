def main():
    _ = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    cur = 1
    pre = A[0]
    for a in A[1:]:
        if pre == a:
            cur += 1
        else:
            ans += cur//2
            cur = 1
        pre = a
    else:
        ans += cur//2
    print(ans)


if __name__ == '__main__':
    main()
