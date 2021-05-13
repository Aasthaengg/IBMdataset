from string import ascii_lowercase


def solve(string):
    n = int(string)
    ans = ""
    while n:
        n, c = divmod(n - 1, len(ascii_lowercase))
        ans = ascii_lowercase[c] + ans
    return ans


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
