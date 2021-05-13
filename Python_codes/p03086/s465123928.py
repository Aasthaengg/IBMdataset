#!/usr/bin/env python3
def main():
    S = input()

    lst = set(['A', 'C', 'G', 'T'])
    cnt = 0
    ans = 0
    for s in S:
        if s in lst:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
