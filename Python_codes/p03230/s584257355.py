def solve(n):
    k = 1
    while k * (k + 1) < 2 * n:
        k += 1
    if k * (k + 1) != 2 * n:
        return False, [], -1
    ans = [[] for _ in range(1000)]
    add_num = 1
    ans[1].append(add_num)
    ans[0].append(add_num)
    for i in range(2, k + 1):
        for j in range(i):
            add_num += 1
            ans[i].append(add_num)
            ans[i - j - 1].append(add_num)
    return True, ans, k


def main():
    n = int(input())
    res, ans, k = solve(n)
    if res:
        print("Yes")
        print(k + 1)
        for a in ans:
            if a:
                print(len(a), " ".join(map(str, a)))
            else:
                break
    else:
        print("No")


if __name__ == '__main__':
    main()
