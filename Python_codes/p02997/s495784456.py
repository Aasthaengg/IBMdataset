def solve(string):
    n, k = map(int, string.split())
    if k > (n - 1) * (n - 2) // 2:
        return "-1"
    ans = []
    c = (n - 1) * (n - 2) // 2
    for i in range(1, n):
        ans.append("{} {}".format(i, n))
    for i in range(1, n):
        for j in range(i + 1, n):
            if c - k == 0:
                break
            c -= 1
            ans.append("{} {}".format(i, j))
    return "{}\n".format(len(ans)) + "\n".join(ans)


if __name__ == '__main__':
    print(solve(input()))
