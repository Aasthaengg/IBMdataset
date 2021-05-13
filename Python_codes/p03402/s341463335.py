import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    """
    解説聞いたらそりゃそうなんだが、どうやったらスラスラ思いつくんだ。。。
    """
    ans1 = [['.'] * 100 for _ in range(50)]
    for i in range(b // 49):
        for j in range(49):
            ans1[i * 2 + 1][j * 2 + 1] = '#'
    for j in range(b % 49):
        ans1[b // 49 * 2 + 1][j * 2 + 1] = '#'

    ans2 = [['#'] * 100 for _ in range(50)]
    for i in range(a // 49):
        for j in range(49):
            ans2[i * 2 + 1][j * 2 + 1] = '.'
    for j in range(a % 49):
        ans2[a // 49 * 2 + 1][j * 2 + 1] = '.'

    ans = ans1 + ans2
    print(100, 100)
    for i in range(100):
        print("".join(ans[i]))


if __name__ == "__main__":
    main()
