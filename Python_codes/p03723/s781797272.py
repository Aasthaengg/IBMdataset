#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    ans = 0
    already = set()
    already.add((A, B, C))
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        tmp_a = B // 2 + C // 2
        tmp_b = A // 2 + C // 2
        tmp_c = B // 2 + A // 2
        A = tmp_a
        B = tmp_b
        C = tmp_c
        ans += 1

        res = (A, B, C)
        if res in already:
            ans = -1
            break
        already.add(res)

    ans = ans if ans else 0
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == "__main__":
    main()