def solve(N):
    if len(N) > 1:
        tmp = N[0] + '9' * (len(N) - 1)
    else:
        print(int(N))
        exit()

    if int(tmp) > int(N):
        tmp = str(int(N[0]) - 1) + '9' * (len(N) - 1)

    ans = 0
    for s in tmp:
        ans += int(s)

    return ans


if __name__ == "__main__":
    N = input()
    print(solve(N))
