def main():
    import sys
    input = sys.stdin.readline
    from fractions import gcd

    N, M = map(int, input().split())
    A = list(set(map(lambda x: int(x)//2, input().split())))

    l = 1
    div2_count = count_div2(A[0])

    for a in A:
        l = l*a // gcd(l, a)
        c = count_div2(a)
        if div2_count != count_div2(a):
            print(0)
            exit()
    #     div2_count.append(max(count_div2(a), 1))
    # print(div2_count)
    # l *= min(div2_count)
    # print(l)
    # l の奇数倍が1より大きくM以下にいくつあるか

    print((M//l + 1)//2)


def count_div2(x):
    ans = 0
    while x % 2 == 0:
        x = x//2
        ans += 1
    return ans


if __name__ == "__main__":
    main()
