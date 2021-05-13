def solve(string):
    n, k = map(int, string.split())
    c = (n - 1) * (n - 2) // 2 - k
    if c < 0:
        return "-1"
    ans = [str(n - 1 + c)]
    for i in range(1, n):
        ans.append("{} {}".format(i, n))
    for i in range(1, n):
        for j in range(i + 1, n):
            if c == 0:
                break
            c -= 1
            ans.append("{} {}".format(i, j))
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve(input()))
