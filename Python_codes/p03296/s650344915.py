def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    pre = A[0]
    changed = False
    for a in A[1:]:
        if changed:
            changed = False
        elif pre == a:
            ans += 1
            changed = True
        pre = a
    print(ans)


if __name__ == '__main__':
    main()
