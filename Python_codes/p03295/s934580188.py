import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    rule = [[] for _ in range(n)]
    for i in range(m):
        rule[data[i][0] - 1].append(data[i][1])
        rule[data[i][1] - 1].append(data[i][0])
    res = rule[0][:]
    ans = 0
    for j in range(n - 1):
        if j + 2 not in res:
            res.extend(rule[j + 1])
        else:
            ans += 1
            res = rule[j + 1][:]
    print(ans)


if __name__ == '__main__':
    main()