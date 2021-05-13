from collections import deque


def p_f():
    m, k = map(int, input().split())
    length = 1 << (m + 1)
    n = 1 << m
    if n <= k:
        print(-1)
        exit()

    if m == 1 and k == 0:
        print("0 0 1 1")
        exit()
    elif m == 1 and k == 1:
        print(-1)
        exit()

    d = deque()
    d.append(k)
    for i in range(n):
        if i == k:
            continue
        d.append(i)
        d.appendleft(i)
    d.append(k)
    print(*d)


if __name__ == '__main__':
    p_f()
