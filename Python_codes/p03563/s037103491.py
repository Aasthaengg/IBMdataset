def solve(string):
    r, g = map(int, string.split())
    return str(2 * g - r)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
