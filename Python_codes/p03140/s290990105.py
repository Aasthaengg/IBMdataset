def main():
    N = int(input())
    A = [input() for i in range(3)]
    ans = 0
    for i in range(N):
        cur = {A[0][i], A[1][i], A[2][i]}
        # print(cur)
        ans += (len(cur) - 1)
    print(ans)


if __name__ == '__main__':
    main()
