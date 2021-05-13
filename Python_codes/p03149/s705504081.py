def main():
    N = list(map(int, input().split()))
    ans = [False]*4
    for n in N:
        if n == 1:
            ans[0] = True
        elif n == 9:
            ans[1] = True
        elif n == 7:
            ans[2] = True
        elif n == 4:
            ans[3] = True
    if all(ans):
        print("YES")
    else:
        print("NO")

    return 0

if __name__ == '__main__':
    main()