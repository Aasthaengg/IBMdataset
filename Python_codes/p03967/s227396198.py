def main():
    import sys
    input = sys.stdin.readline
    s = input().rstrip('\n')
    t = len(s)
    mp = t // 2
    mg = t - mp
    import collections
    s = collections.Counter(s)
    print(mp - s["p"])


if __name__ == '__main__':
    main()
