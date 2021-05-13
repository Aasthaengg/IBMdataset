#!/usr/bin/env python3
def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    S = input().rstrip()
    Q = int(input())

    S = deque(S)
    rev = 0
    for _ in [0] * Q:
        q = input().split()
        if q[0] == '1':
            rev += 1
        else:
            if q[1] == '1':
                S.append(q[2]) if rev % 2 else S.appendleft(q[2])
            else:
                S.appendleft(q[2]) if rev % 2 else S.append(q[2])
    ans = ''.join(S)
    print(ans[::-1] if rev % 2 else ans)


if __name__ == '__main__':
    main()
