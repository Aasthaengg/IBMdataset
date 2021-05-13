def log2(n):
    i = 1
    r = 0
    if n < 0:
        i = 2
        r = 1
        n = -n
    s = i
    while n > s:
        i *= 4
        s += i
        r += 2
    return r


def resolve():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = [0] * 40
    while n:
        l = log2(n)
        ans[l] += 1
        n = n - (-2) ** l
    while ans[-1] == 0:
        ans.pop()
    print("".join([str(x) for x in ans[::-1]]))


if __name__ == '__main__':
    resolve()
