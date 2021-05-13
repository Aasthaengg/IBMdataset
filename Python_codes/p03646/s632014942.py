def main():
    K = int(input())
    N = 50
    ans = [i for i in range(N)]
    d = K//50
    r = K % 50
    if K != 0:
        for i in range(r):
            for j in range(N):
                if i == j:
                    ans[j] += N
                else:
                    ans[j] -= 1
        for i in range(N):
            ans[i] += d
    print(N)
    print(*ans)


if __name__ == '__main__':
    main()
